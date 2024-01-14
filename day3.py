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
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            num = ''
            char = grid[symbol[0] + i][symbol[1] + j]

            if i == 0 and j == 0:
                # This is the symbol coordinates
                break

            offset = j
            while char.isdigit():
                # Check for more digits to the left
                if j == -1:
                    num = char + num
                    offset -= 1
                    if symbol[1] + offset >= 0:
                        char = grid[symbol[0] + i][symbol[1] + offset]
                    else:
                        # Reached start of row
                        break
                else:
                    # Check for more digits to the right, avoiding overlapping checks
                    num = num + char
                    offset += 1
                    # TODO: don't check j = 1 if both j = 0 and j = 1 are digits
                    try:
                        char = grid[symbol[0] + i][symbol[1] + offset]
                    except IndexError:
                        break

            if num:
                numbers.append(int(num))