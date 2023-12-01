import os

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)

# Store total calotries held by each elf
calibration = []

# Parse input calories
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    for line in f:
        calibration.append(line.strip())

val = 0
for line in calibration:
    try:
        for c in line:
            if c.isnumeric():
                val += int(c) * 10
                break
        for c in line[::-1]:
            if c.isnumeric():
                val += int(c)
                break
    except ValueError:
        pass

print(val)

tokens = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
