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

# Preprocess the input strings to pairs
class Location:
    def __init__(self, val, pos) -> None:
        self.val = val
        self.pos = pos
    def __repr__(self) -> str:
        return f"val: {self.val} pos: {self.pos}"
    
# PART 1
# 1. Convert the lines to list of list of integers
_items = []
for line in store:
    _items.append([int(x) for x in line.split(" ") if x])
first_items = []
second_items = []
for idx in range(len(_items)):
    first_items.append(Location(_items[idx][0], idx))
    second_items.append(Location(_items[idx][1], idx))
# 2. Sort the items based on the distance in the lists
first_items.sort(key=lambda x: x.val)
second_items.sort(key=lambda x: x.val)
# 3. Compute the total distance
total_distance = 0
for idx in range(len(first_items)):
    first_val = first_items[idx].val
    first_pos = first_items[idx].pos
    second_val = second_items[idx].val
    second_pos = second_items[idx].pos
    distance = abs(first_val - second_val)
    total_distance += distance
print(total_distance)

# PART 2
from collections import Counter
# 1. Convert the lines to list of list of integers
first_items = []
second_items = []
for idx in range(len(_items)):
    first_items.append(_items[idx][0])
    second_items.append(_items[idx][1])
# 2. Sort the second list into the Counter class
counter = Counter(second_items)
# print(counter)
similarity_score = 0
for val in first_items:
    if val in counter.keys():
        # print(f"{val} exists")
        similarity_score += val * counter[val]
print(similarity_score)
