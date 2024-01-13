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

# Search areas adjacent to symbols

# Continue reading numbers if a digit is adjacent to a symbol
# Try to avoid double checking areas if there are symbols adjacent to each other