import os

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

commands = []
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    for line in f:
        cmd = line.strip().split(" ")
        if len(cmd) > 1:
            cmd[1] = int(cmd[1])
        commands.append(cmd)

# Puzzle 1
X = 1
cycle = 0
signal = 0


def cycle_check(cycle: int, x: int) -> int:
    if cycle not in [20, 60, 100, 140, 180, 220]:
        return 0

    return cycle * x


for cmd in commands:
    if "noop" in cmd:
        cycle += 1
        signal += cycle_check(cycle, X)

    elif "addx" in cmd:
        left = 2
        while left > 0:
            left -= 1
            cycle += 1
            signal += cycle_check(cycle, X)

        X += cmd[1]

print(signal)
