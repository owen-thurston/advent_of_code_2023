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
adjacency_masks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for symbol in symbols:

    # Check 8 spaces adjacent to symbol using adjacency_mask
    for mask in adjacency_masks:
        char = grid[symbol[0] + mask[0]][symbol[1] + mask[1]]

        if not char == '.' and char.isdigit():
            # Continue reading numbers if a digit is adjacent to a symbol

# Avoid double checking areas if there are symbols adjacent to each other