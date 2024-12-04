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

sum = 0
pattern = r"mul\(\d+,\d+\)"
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
# print(sum)

def part_1(info):    
    sum = 0
    pattern = r"mul\(\d+,\d+\)"
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
    return sum

# Part 2
data_file2 = "test_data.txt"
# data_file2 = "data_2.txt"
info2 = ""
with open(f"{ROOT_DIR}/{data_file2}", "r") as f:
    info2 = f.read()
# print(info2)

# Append do() infront as it starts ith do()
info = "do()" + info2

# Scan for all do()
sum = 0
do_indexes = find_all_occurrences(info, "do()")
dont_indexes = find_all_occurrences(info, "don't()")
class Command:
    def __init__(self, cmd, idx):
        self.cmd = cmd
        self.idx = idx
commands = []
for idx in do_indexes:
    cmd = Command("do", idx)
    commands.append(cmd)
for idx in dont_indexes:
    cmd = Command("dont", idx)
    commands.append(cmd)
commands.append(Command("dont", len(info)))
commands = sorted(commands, key=lambda x: x.idx)

# print(info2)
for i in range(len(commands)-1):
    # print(commands[i].cmd, commands[i+1].cmd)
    if commands[i].cmd == "do" and commands[i].cmd == "do":
        ss = info[commands[i].idx:commands[i+1].idx]
        # print(ss)
        sum += part_1(ss)
    elif commands[i].cmd == "do" and commands[i].cmd == "dont":
        ss = info[commands[i].idx:commands[i+1].idx]
        # print(ss)
        sum += part_1(ss)
        pass
    elif commands[i].cmd == "dont" and commands[i].cmd == "do":
        pass
    elif commands[i].cmd == "dont" and commands[i].cmd == "dont":
        pass
    else:
        pass
print(sum)
