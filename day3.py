# Read input into 2x2 grid
grid = []

with open('test.txt', 'r') as f:
    for row in f:
        grid.append(list(row.strip()))

# Find symbol coordinates
symbols = []
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if not (val == '.' or val.isdigit()):
            symbols.append((i, j))

numbers = []

# Search areas adjacent to symbols
for symbol in symbols:

    # Check 8 spaces adjacent to symbol starting upper left
    offset = -1
    num = ''
    char = grid[symbol[0] -1][symbol[1] + offset]

    # Continue reading numbers if a digit is adjacent to a symbol
    while char.isdigit():
        num = char + num
        offset -= 1
        if symbol[1] + offset >= 0:
            char = grid[symbol[0] -1][symbol[1] + offset]
        else:
            break

    # Rows
    # TODO: trying to write up a loop approach
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            num = ''
            char = grid[symbol[0] + i][symbol[1] + offset]

# Avoid double checking areas if there are symbols adjacent to each other