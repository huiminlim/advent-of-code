import os
from turtle import color

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# print(ROOT_DIR)

# Parse input strings
store = []
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    for line in f:
        store.append(line.strip())

# Process and parse the input strings
game_info = {}
for idx in range(len(store)):
    line = store[idx]
    game_id =  int(line.split(":")[0].split(" ")[1])
    set_info = line.split(":")[1].split(";")

    # populate the game info
    game_info[game_id] = []

    # parse the cubes revealed from the bag in the sets
    for set in set_info:
        cubes = set.split(",")
        set_data = {}
        for cube in cubes:
            cube = cube.strip()
            num_cube = int(cube.split(" ")[0])
            color_cube = cube.split(" ")[1]
            set_data[color_cube] = num_cube
        game_info[game_id].append(set_data)

# Attempt to solve part 1
total_val = 0
for game_id, infos in game_info.items():
    game_not_possible = False
    for info in infos:
        for cube_color, count in info.items():
            exceed_red = cube_color == "red" and count > 12
            exceed_blue = cube_color == "blue" and count > 14
            exceed_green = cube_color == "green" and count > 13
            if exceed_blue or exceed_green or exceed_red:
                game_not_possible = True
                break
    if not game_not_possible:
        total_val += game_id
print(total_val)

# Attempt to solve part 2
total_val = 0
for game_id, infos in game_info.items():
    prev_cube_count = {"red": 0, "blue": 0, "green": 0}
    for info in infos:
        for cube_color, count in info.items():
            if count > prev_cube_count[cube_color]:
                prev_cube_count[cube_color] = count
    power = 1
    for count in prev_cube_count.values():
        power *= count
    total_val += power
print(total_val)
