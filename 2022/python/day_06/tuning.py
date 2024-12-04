import os

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

stream = ""
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    stream = f.readline()

# Puzzle 1
# Find how many characters processed for marker to be present
start_idx = 0
last_idx = 3
while last_idx < len(stream):
    sequence = stream[start_idx:last_idx + 1]

    if len(set(sequence)) == 4:
        break

    start_idx += 1
    last_idx += 1

print(last_idx + 1)

# Puzzle 2
# Find how many characters processed for marker to be present
start_idx = 0
last_idx = 14 - 1
while last_idx < len(stream):
    sequence = stream[start_idx:last_idx + 1]

    if len(set(sequence)) == 14:
        break

    start_idx += 1
    last_idx += 1

print(last_idx + 1)
