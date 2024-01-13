# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
import re
from functools import reduce

games = []

with open("day2_input.txt", "r") as f:
    cubes = {"red": 12, "green": 13, "blue": 14}
    impossible_games_id_sum = 0

    # test if ids are complete and in order to be able to put them in a list
    i = 1
    for game in f:
        match = re.match(r"Game (\d+):", game)
        assert match.group(1) == str(i), game
        i += 1

    f.seek(0)  # Reset file pointer to start of file

    # Parse data and check for possible games and collect ids
    # and read games into a data structure (for possible pt 2?)
    for game in f:
        match = re.match(r"^Game (\d+): (.+)$", game)
        draw_set = []
        game_possible = True
        for ds in match.group(2).split(";"):
            draw = {}
            for dg in ds.strip().split(","):
                d = dg.strip().split(" ")
                draw_key = d[1].lower()
                draw_val = int(d[0])
                draw[draw_key] = draw_val

                # assume more possible than impossible games
                # if game is impossible, skip check for the rest of the game
                if game_possible and draw_val > cubes[draw_key]:
                    impossible_games_id_sum += len(games) + 1
                    game_possible = False
            draw_set.append(draw)
        games.append(draw_set)

    # Calculate sum of ids of possible games
    # n*(n+1)/2
    n = len(games)
    total = (n * (n + 1)) / 2
    total -= impossible_games_id_sum
    # print(total)

## Part 2
power_sum = 0
for game in games:
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    
    for draw in game:
        for k, v in draw.items():
            if v > min_cubes[k]:
                min_cubes[k] = v
    
    power_sum += reduce(lambda x, y: x * y, min_cubes.values(), 1)

print(power_sum)