# Read input into 2x2 grid
grid = []

with open('test.txt', 'r') as f:
    for row in f:
        grid.append(list(row.strip()))

# Find symbol coordinates
symbols = []
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if not val.isdigit():
            symbols.append((i, j))
print(symbols)

# Search areas adjacent to symbols
# Try to avoid double checking areas if there are symbols adjacent to each other