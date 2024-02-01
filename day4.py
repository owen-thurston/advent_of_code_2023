points = 0

with open('day4_input.txt', 'r') as f:
    for line in f:
        # Parse input line
        numbers = line.split(": ")[1].split(' | ')

        # create sets
        winning_numbers = set(numbers[0].split())
        my_numbers = set(numbers[1].split())

        # Measure size of set intersection
        num_winning = len(winning_numbers & my_numbers)

        # Allocate points
        if num_winning > 0:
            points += 2 ** (num_winning - 1)
print(points)