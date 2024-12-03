import os

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#print(ROOT_DIR)

# Data file name
# data_file = "test_data.txt"
data_file = "data.txt"

# Parse input strings
info = ""
with open(f"{ROOT_DIR}/{data_file}", "r") as f:
    info = f.read()

# Part 1
def find_all_occurrences(s, sub):
    start = 0
    indices = []
    while True:
        start = s.find(sub, start)
        if start == -1:
            break
        indices.append(start)
        start += len(sub)  # Move past the last found substring
    return indices

def find_nearest_occurrence(s, char):
    return s.find(char)

import re
pattern = r"mul\(\d+,\d+\)"

sum = 0
indexes = find_all_occurrences(info, "mul")
for idx in indexes:
    # print(idx)
    ss = info[idx:]
    # find (
    idx1 = find_nearest_occurrence(ss, "(")
    if idx1 != 3:
        # print(f"Rejected: {ss}")
        continue
    idx2 = find_nearest_occurrence(ss, ")")
    # Extract the multiplication
    ss2 = ss[0:idx2+1]
    # print(ss2)
    matches = re.fullmatch(pattern, ss2)
    # print(ss2, matches)
    if matches != None:
        # print("Matched")
        ss2 = ss2.replace("mul(", "")
        ss2 = ss2.replace(")", "")
        sum += int(ss2.split(",")[0]) * int(ss2.split(",")[1])  
print(sum)
