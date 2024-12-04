import os
from collections import deque

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

moves = []
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    for i, line in enumerate(f):
        if i >= 10:
            tokens = line.strip().split()
            moves.append({"count": int(tokens[1]), "start": int(tokens[3]), "dest": int(tokens[5])})

# Puzzle 1
# Setup the stacks
stacks = []
stacks.append(deque())  # first index 0 is not used
stacks.append(deque(['F', 'L', 'M', 'W']))
stacks.append(deque(['F', 'M', 'V', 'Z', 'B']))
stacks.append(deque(['Q', 'L', 'S', 'R', 'V', 'H']))
stacks.append(deque(['J', 'T', 'M', 'P', 'Q', 'V', 'S', 'F']))
stacks.append(deque(['W', 'S', 'L']))
stacks.append(deque(['W', 'J', 'R', 'M', 'P', 'V', 'F']))
stacks.append(deque(['F', 'R', 'N', 'P', 'C', 'Q', 'J']))
stacks.append(deque(['B', 'R', 'W', 'Z', 'S', 'P', 'H', 'V']))
stacks.append(deque(['W', 'Z', 'H', 'G', 'C', 'J', 'M', 'B']))

# Perform the moving of individual crates
for move in moves:
    count = move["count"]
    start = stacks[move["start"]]
    dest = stacks[move["dest"]]

    for _ in range(count):
        dest.appendleft(start.popleft())

# Get top most crates
print("".join([s[0] for i, s in enumerate(stacks) if i > 0]))

# Puzzle 2
# Setup the stacks
stacks = []
stacks.append(deque())  # first index 0 is not used
stacks.append(deque(['F', 'L', 'M', 'W']))
stacks.append(deque(['F', 'M', 'V', 'Z', 'B']))
stacks.append(deque(['Q', 'L', 'S', 'R', 'V', 'H']))
stacks.append(deque(['J', 'T', 'M', 'P', 'Q', 'V', 'S', 'F']))
stacks.append(deque(['W', 'S', 'L']))
stacks.append(deque(['W', 'J', 'R', 'M', 'P', 'V', 'F']))
stacks.append(deque(['F', 'R', 'N', 'P', 'C', 'Q', 'J']))
stacks.append(deque(['B', 'R', 'W', 'Z', 'S', 'P', 'H', 'V']))
stacks.append(deque(['W', 'Z', 'H', 'G', 'C', 'J', 'M', 'B']))

# Perform the moving sets of crates
for move in moves:
    count = move["count"]
    start = stacks[move["start"]]
    dest = stacks[move["dest"]]

    crates = []
    for _ in range(count):
        crates.append(start.popleft())

    for crate in reversed(crates):
        dest.appendleft(crate)

# Get top most crates
print("".join([s[0] for i, s in enumerate(stacks) if i > 0]))
