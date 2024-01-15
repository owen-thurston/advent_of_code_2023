# Create boolean adjacency grids for symbols and numbers
# Take ^ of grids to find out which numbers to keep
from pprint import pprint

# Read input into 2x2 grid
grid = []

with open('test.txt', 'r') as f:
    for row in f:
        grid.append(list(row.strip()))

# Make grid for symbols and numbers
symbol_grid = [[False for x in range(len(grid[0]))] for x in range(len(grid))]

def mark_adjacent_cells(grid, x, y):
    # If there are adjacent symbols, some cells will be marked extra times
    # Accepted as simplicity trade-off
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if x + i < 0 or y + j < 0:
                # Start of row already reached
                return
            try:
                grid[x + i][y + j] = True
            except IndexError:
                # End of row already reached
                return

# Populate symbol adjacency grid
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if not (val == '.' or val.isdigit()):
            mark_adjacent_cells(symbol_grid, i, j)

pprint(symbol_grid)