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

# Puzzle 2
# - If sprite is positioned such that one of its
#   three pixels is the pixel currently being drawn,
#   the screen produces a lit # pixel, else dark .


def draw(cycle, crt, sprite):

    if cycle % 40 == 0 and cycle != 0:
        crt.append([])

    current_pix_drawing = len(crt[-1])
    if current_pix_drawing in sprite:
        crt[-1].append("#")
    else:
        crt[-1].append(".")


crt = [[]]
sprite = [0, 1, 2]
cycle = 0
for cmd in commands:
    if "noop" in cmd:
        draw(cycle, crt, sprite)
        cycle += 1

    elif "addx" in cmd:
        left = 2
        while left > 0:
            draw(cycle, crt, sprite)
            left -= 1
            cycle += 1

        sprite = [x + cmd[1] for x in sprite]


for row in crt:
    for pix in row:
        print(pix, end="")
    print()
