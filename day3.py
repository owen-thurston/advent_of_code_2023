# Create boolean adjacency grids for symbols and numbers
# Take ^ of grids to find out which numbers to keep

# Read input into 2x2 grid
grid = []

with open('day3_input.txt', 'r') as f:
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

# Check which numbers overlap with adjacency grid
numbers = []
num = ''
adjacent = False

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val.isdigit():
            num += val
            adjacent |= symbol_grid[i][j]
        elif num != '':
            if adjacent:
                numbers.append(int(num))
            num = ''
            adjacent = False

print(sum(numbers))

# Part 2
# Find '*' symbols with 2 numbers adjacent to them
def num_adjacent(grid, x, y):
    num_adj = 0

    for i in (-1, 0, 1):
        last_adj = False
        for i in (-1, 0, 1):
            if grid[x][y].isdigit() and not last_adj:
                num_adj += 1
                last_adj = True
            else:
                last_adj = False

    return num_adj

gear_ratios = []

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == '*' and num_adjacent(grid, i, j) == 2:
            # This is a gear. Get gear ratio
            