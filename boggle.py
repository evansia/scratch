
def search(grid, x, y, wordSoFar, wordDict, seen, result):
    loc = str(x)+str(y)
    if loc in seen:
        return
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid):
        return
    if wordSoFar in wordDict and len(wordSoFar) >= 3 and wordSoFar not in result:
        print(wordSoFar)
        result.add(wordSoFar)
    seen.add(loc)
    word = wordSoFar+grid[x][y]
    search(grid, x+1, y, word, wordDict, seen, result)
    search(grid, x-1, y, word, wordDict, seen, result)
    search(grid, x, y+1, word, wordDict, seen, result)
    search(grid, x, y-1, word, wordDict, seen, result)
    search(grid, x+1, y+1, word, wordDict, seen, result)
    search(grid, x-1, y-1, word, wordDict, seen, result)
    seen.remove(loc)

def generate_word_dict():
    with open('boggle_dict.txt') as f:
        wordDict = set(f.read().splitlines())
    return wordDict

def generate_grid():
    grid_in_str = 'AALSYPCSWNSNTEGO'
    grid = []
    count = 0
    for i in range(0, 4):
        row = []
        for j in range(0, 4):
            row.append(grid_in_str[count])
            count += 1
        grid.append(row)
    print(grid)
    return grid

def look_for_answers(grid, wordDict):
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            search(grid, x, y, '', wordDict, set(), set())

wordDict = generate_word_dict()
grid = generate_grid()
look_for_answers(grid, wordDict)

