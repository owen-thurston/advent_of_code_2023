# Read input into 2x2 grid
grid = []

with open('test.txt', 'r') as f:
    for row in f:
        grid.append(list(row.strip()))

# Make grid for symbols and numbers
symbol_grid = []
number_grid = []

def mark_adjacent_cells(grid, x, y):
    # If there are adjacent symbols, some cells will be marked extra times
    # Accepted as simplicity trade-off
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            # FIXME: out of bounds errors
            try:
                grid[x + i][y + i] = True
            except IndexError

# Populate grids
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == '.':
            continue
        elif val.isdigit():
            mark_adjacent_cells(number_grid, i, j)
        else:
            mark_adjacent_cells(symbol_grid, i, j)
