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

################### Part 2 #######################
# Find '*' symbols with 2 numbers adjacent to them
def num_adjacent(grid, x, y):
    """ Returns number of separate numbers adjacent to provided coordinate"""
    num_adj = 0

    for i in (-1, 0, 1):
        # last_adj ensures sequential digits aren't counted separately
        last_adj = False
        for j in (-1, 0, 1):
            if grid[x + i][y + j].isdigit():
                if not last_adj:
                    num_adj += 1
                    last_adj = True
            else:
                last_adj = False

    return num_adj

def get_gear_ratio(grid, x, y):
    num1 = ''
    num2 = ''

    for i in (-1, 0, 1):
        # last_digit indicates if the previous loop iteration char was a digit
        if num1 and not num2:
            last_digit = False
            num2 = num1
            num1 = ''
        last_digit = False

        for j in (-1, 0, 1):
            if grid[x + i][y + j].isdigit():
                # TODO: right guarded by j=1 and left guarded by j=-1
                # TODO: last_digit determines if the 3x3 numbers are connected
                num1 = num1 + grid[x + i][y + j]

                if j == -1:
                    # Collect digits going left but not past list limits
                    # As well as collect digits in the 3x3 space around the "*"
                    k = j - 1
                    while y + k >= 0 and grid[x + i][y + k].isdigit():
                        num1 = grid[x + i][y + k] + num1
                        k -= 1
                elif j == 1:
                    # Collect digits going right until a gap reached and not past list limits
                    k = j + 1
                    try:
                        while grid[x + i][y + k].isdigit():
                            num1 = num1 + grid[x + i][y + k]
                            k += 1
                    except IndexError:
                        # End of row reached
                        pass
                last_digit = True
            elif num1 and not num2:
                last_digit = False
                num2 = num1
                num1 = ''
    
    return int(num1) * int(num2)

gear_ratios = []

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        # DEBUG
        # if i == 14 and j == 70:
        #     pass
        if val == '*' and num_adjacent(grid, i, j) == 2:
            # DEBUG
            print(f"({i}, {j})")
            # This is a gear. Get gear ratio
            gear_ratios.append(get_gear_ratio(grid, i, j))
print(sum(gear_ratios))