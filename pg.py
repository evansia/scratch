import psycopg2
import datetime

src_conn = psycopg2.connect(host="localhost",database="source_test", user="source", password="source",port="15432")
dest_conn = psycopg2.connect(host="localhost",database="business_intelligence_development", user="postgres", password=<YOUR_LOCAL_PG_PASSWORD_IF_AVAIL>)
src_cursor = src_conn.cursor()
dest_cursor = dest_conn.cursor()

dest_cursor.execute('truncate table daily_user_journals')
src_cursor.execute("""SELECT
    team_id,
    whiteboard_id,
    job_title,
    user_id,
    manager_id,
    days.at as at
FROM positions
CROSS JOIN (
  SELECT
    date_trunc('day', generate_series) as at
  FROM
    generate_series(now() - interval '1 year', now(), '1 day'::interval)
) AS days
WHERE
    (positions.started_at <= now()) AND (positions.ended_at IS NULL OR positions.ended_at >= now())
ORDER BY positions.id DESC""")
res = src_cursor.fetchall()
for rec in res:
    dest_cursor.execute("insert into daily_user_journals(pistachio_team_id,pistachio_whiteboard_id,pistachio_user_job_title,pistachio_user_id,pistachio_manager_id,date) values (%s,%s,%s,%s,%s,%s)",(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5]))
    print(rec)

dest_conn.commit()
src_cursor.close()
dest_cursor.close()
src_conn.close()