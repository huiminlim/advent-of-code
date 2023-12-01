import os

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)

# Store total calotries held by each elf
elves = []

# Parse input calories
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    curr_sum = 0
    for line in f:
        if line.strip() == "":
            elves.append(curr_sum)
            curr_sum = 0
        else:
            curr_sum += int(line)

# Puzzle 1
# Get the max aggregated calories
max_calories = max(elves)

# Puzzle 2
# Get the sum of top 3 max calories
sum_max_calories = sum(sorted(elves, reverse=True)[0:3])
