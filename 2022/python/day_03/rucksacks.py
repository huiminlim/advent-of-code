import os

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def compute_priority(char: str) -> int:

    # Uppercase
    if ord(char) >= 65 and ord(char) <= 90:
        priority = 27 + (ord(char) - 65)

    # Lowercase
    else:
        # 97 is the ascii value of 'a', which has priority of 1
        priority = ord(char) - 97 + 1

    return priority


# For puzzle 1
# Iterate through each item and compute the priority
# A priority is the value of the common item
items = []
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    for line in f:
        tmp = line.strip().split(" ")[0]
        first, second = tmp[:len(tmp) // 2], tmp[len(tmp) // 2:]
        items.append((first, second))

total_priority = 0
for item in items:
    (first, second) = item
    first = set([x for x in first])
    second = set([x for x in second])
    common = first.intersection(second).pop()
    total_priority += compute_priority(common)

print(total_priority)

# For puzzle 2
elves = []
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    for line in f:
        elves.append(line.strip().split(" ")[0])

total_priority = 0
for idx in range(0, len(elves), 3):
    first = set(elves[idx])
    second = set(elves[idx + 1])
    third = set(elves[idx + 2])
    common = first.intersection(second).intersection(third).pop()
    total_priority += compute_priority(common)

print(total_priority)
