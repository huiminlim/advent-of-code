import os

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#print(ROOT_DIR)

# Data file name
# data_file = "test_data.txt"
data_file = "data.txt"

# Parse input strings
store = []
with open(f"{ROOT_DIR}/{data_file}", "r") as f:
    for line in f:
        store.append(line.strip())

# Part 1
num_safe = 0
for line in store:
    vals = line.split(" ")
    vals = [int(x) for x in vals]
    # print(vals)

    # Check if is all increasing/decreasing
    if vals[0] < vals[-1]:
        # increasing
        if sorted(vals) != vals:
            continue
        # else:
        #     print("increasing")
    else:
        # decreasing
        if sorted(vals, reverse=True) != vals:
            continue
        # else:
        #     print("decreasing")

    # Check if delta between each value is "differ by at least one and at most three"
    for idx in range(len(vals)-1):
        delta = abs(vals[idx+1] - vals[idx])
        is_safe = delta >= 1 and delta <=3
        # print(delta)
        if not is_safe:
            break
    if is_safe:
        num_safe += 1
print(num_safe)

# Part 2
