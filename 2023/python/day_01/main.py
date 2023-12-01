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


tokens = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tokens2 = ["z0o", "o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"]

# print(calibration)
for i in range(len(calibration)):
    line = calibration[i]
    for ci in range(len(line)):
        substr = line[ci:]
        for ti in range(len(tokens)):
            replacement = ""
            token = tokens[ti]
            if substr.startswith(token):
                replacement = f"{tokens2[ti]}"
            if replacement != "":
                calibration[i] = calibration[i].replace(token, replacement)
                break
# print(calibration)

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