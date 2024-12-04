import os
from collections import defaultdict

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

moves = []
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    for line in f:
        move = line.strip().split(" ")
        move[1] = int(move[1])
        moves.append(move)

# Logics:
# - Touching means diagonally adjacent or overlap
# - If head is ever 2 steps directly up/down/left/right from tail,
#   tail must move 1 step in direction
# - If head and tail aren't touching and aren't in the same row/col
#   tail always moves one step diagonal to keep up

# Puzzle 1
xhead, yhead = 0, 0
xtail, ytail = 0, 0
tail_pos = defaultdict(lambda: 0)
tail_pos[(xtail, ytail)] = 1

xsigns = {"R": 1, "L": -1, "U": 0, "D": 0}
ysigns = {"R": 0, "L": 0, "U": 1, "D": -1}

for move in moves:
    # Extract the steps to execute for head
    xsign = xsigns[move[0]]
    ysign = ysigns[move[0]]
    steps = move[1]

    while steps > 0:
        steps -= 1
        yhead += ysign
        xhead += xsign

        # Derive the tail pos according to logic
        if xhead == xtail and yhead != ytail:
            if yhead - ytail == 2:
                ytail += 1
            elif ytail - yhead == 2:
                ytail -= 1
        elif yhead == ytail and xhead != xtail:
            if xhead - xtail == 2:
                xtail += 1
            elif xtail - xhead == 2:
                xtail -= 1
        elif not (ytail == yhead and xhead == xtail) and (abs(xtail - xhead) >= 2 or abs(ytail - yhead) >= 2):
            if xhead > xtail and yhead > ytail:
                xtail += 1
                ytail += 1
            elif xhead > xtail and yhead < ytail:
                xtail += 1
                ytail -= 1
            elif xhead < xtail and yhead > ytail:
                xtail -= 1
                ytail += 1
            else:
                xtail -= 1
                ytail -= 1

        tail_pos[(xtail, ytail)] += 1

print(len(tail_pos.values()))

# Puzzle 2
rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

# Logics:
# - Touching means diagonally adjacent or overlap
# - If head is ever 2 steps directly up/down/left/right from tail,
#   tail must move 1 step in direction
# - If head and tail aren't touching and aren't in the same row/col
#   tail always moves one step diagonal to keep up

tail_pos = defaultdict(lambda: 0)
tail_pos[(0, 0)] = 1
for move in moves:
    # Extract the steps to execute for head
    xsign = xsigns[move[0]]
    ysign = ysigns[move[0]]
    steps = move[1]

    while steps > 0:
        steps -= 1

        # Update the first head
        rope[0] = [rope[0][0] + xsign, rope[0][1] + ysign]

        # TODO: Update the subsequent rope parts
        for idx in range(1, len(rope)):
            front_rope = rope[idx - 1]
            curr_rope = rope[idx]

            xhead = front_rope[0]
            yhead = front_rope[1]

            xtail = curr_rope[0]
            ytail = curr_rope[1]

            # Derive the tail pos according to logic
            changed = False
            if xhead == xtail and yhead != ytail:
                if yhead - ytail == 2:
                    ytail += 1
                    changed = True
                elif ytail - yhead == 2:
                    ytail -= 1
                    changed = True
            elif yhead == ytail and xhead != xtail:
                if xhead - xtail == 2:
                    xtail += 1
                    changed = True
                elif xtail - xhead == 2:
                    xtail -= 1
                    changed = True
            elif not (ytail == yhead and xhead == xtail) and (abs(xtail - xhead) >= 2 or abs(ytail - yhead) >= 2):
                if xhead > xtail and yhead > ytail:
                    xtail += 1
                    ytail += 1
                    changed = True
                elif xhead > xtail and yhead < ytail:
                    xtail += 1
                    ytail -= 1
                    changed = True
                elif xhead < xtail and yhead > ytail:
                    xtail -= 1
                    ytail += 1
                    changed = True
                else:
                    xtail -= 1
                    ytail -= 1
                    changed = True

            rope[idx] = [xtail, ytail]
            if idx == 9 and changed:
                tail_pos[(xtail, ytail)] += 1

print(len(tail_pos.values()))
