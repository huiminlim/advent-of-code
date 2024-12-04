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
num_safe = 0
unsafe_vals = []
for line in store:
    vals = line.split(" ")
    vals = [int(x) for x in vals]
    # print(vals)

    # Check if is all increasing/decreasing
    if vals[0] < vals[-1]:
        # increasing
        if sorted(vals) != vals:
            unsafe_vals.append(vals)
            continue
        # else:
        #     print("increasing")
    else:
        # decreasing
        if sorted(vals, reverse=True) != vals:
            unsafe_vals.append(vals)
            continue
        # else:
        #     print("decreasing")

    # Check if delta between each value is "differ by at least one and at most three"
    for idx in range(len(vals)-1):
        delta = abs(vals[idx+1] - vals[idx])
        is_safe = delta >= 1 and delta <=3
        # print(delta)
        if not is_safe:
            unsafe_vals.append(vals)
            break
    if is_safe:
        num_safe += 1

print(unsafe_vals)
# Safe = Must be strictly increasing/decreasing AND delta is at least 1 and at most 3
def is_strictly_increasing(lst):
    return all(x < y for x, y in zip(lst, lst[1:]))
def is_strictly_decreasing(lst):
    return all(x > y for x, y in zip(lst, lst[1:]))
def is_safe_delta(lst):
    delta = []
    for idx in range(len(lst)-1):
        delta.append(abs(lst[idx] - lst[idx+1]))
    for d in delta:
        if not(d >= 1 and d <= 3):
            return False
    return True

for vals in unsafe_vals:
    for idx in range(len(vals)):
        new_val = vals[:idx] + vals[idx+1:]
        if (is_strictly_decreasing(new_val) or is_strictly_increasing(new_val)) and is_safe_delta(new_val):
            num_safe += 1
            break
print(num_safe)
