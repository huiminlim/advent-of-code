import os

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

lines = []
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    for line in f:
        lines.append(line.strip().split(" ")[0])

# Puzzle 1
pairs = []
total_overlap = 0
for line in lines:
    [first, second] = line.split(",")
    [first_lower_bound, first_upper_bound] = [int(x) for x in first.split("-")]
    [second_lower_bound, second_upper_bound] = [int(x) for x in second.split("-")]

    if first_lower_bound >= second_lower_bound and first_upper_bound <= second_upper_bound \
            or second_lower_bound >= first_lower_bound and second_upper_bound <= first_upper_bound:
        total_overlap += 1

print(total_overlap)

# Puzzle 2
pairs = []
total_overlap = 0
for line in lines:
    [first, second] = line.split(",")
    [first_lower_bound, first_upper_bound] = [int(x) for x in first.split("-")]
    [second_lower_bound, second_upper_bound] = [int(x) for x in second.split("-")]

    first = set(range(first_lower_bound, first_upper_bound + 1))
    second = set(range(second_lower_bound, second_upper_bound + 1))

    if first.intersection(second):
        total_overlap += 1

print(total_overlap)
