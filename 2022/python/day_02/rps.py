import enum
import os

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class Move(enum.IntEnum):
    Rock = 1
    Paper = 2
    Scissor = 3


class Outcome(enum.IntEnum):
    Win = 6
    Lose = 0
    Draw = 3


# Resolve the Outcome
# For puzzle 2
def resolve_outcome(move: str) -> Outcome:
    if move == "X":
        return Outcome.Lose
    elif move == "Y":
        return Outcome.Draw
    else:
        return Outcome.Win


# Resolve the Moves according to opponent or myself
# For puzzle 1
def resolve_move(move: str, opponent=True) -> Move:
    if opponent:
        if move == "A":
            return Move.Rock
        elif move == "B":
            return Move.Paper
        else:
            return Move.Scissor
    else:
        if move == "X":
            return Move.Rock
        elif move == "Y":
            return Move.Paper
        else:
            return Move.Scissor


def puzzle1(opponent: str, me: str) -> int:
    opponent = resolve_move(opponent)
    me = resolve_move(me, opponent=False)

    points = 0

    if(opponent == Move.Paper and me == Move.Scissor) or \
        (opponent == Move.Scissor and me == Move.Rock) or \
            (opponent == Move.Rock and me == Move.Paper):
        points = 6 + int(me)

    elif opponent == me:
        points = 3 + int(me)

    else:
        points = int(me)

    return points


def puzzle2(opponent: str, outcome: str) -> int:
    opponent = resolve_move(opponent)
    outcome = resolve_outcome(outcome)

    points = 0

    # If the outcome is wom. throw the move
    # to win the opponent's move
    if outcome == Outcome.Win:
        points += 6

        if opponent == Move.Paper:
            # throw scissors
            points += int(Move.Scissor)
        elif opponent == Move.Scissor:
            # throw rock
            points += int(Move.Rock)
        else:
            # throw paper
            points += int(Move.Paper)

    elif outcome == Outcome.Draw:
        points += 3 + int(opponent)

    # If the outcome is lost, then throw the losing
    # move compared to the opponent
    else:
        if opponent == Move.Paper:
            # throw rock
            points += int(Move.Rock)
        elif opponent == Move.Scissor:
            # throw paper
            points += int(Move.Paper)
        else:
            # throw scissor
            points += int(Move.Scissor)

    return points


input = []
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    for line in f:
        tmp = line.strip().split(" ")
        input.append(tmp)

# Puzzle 1
# Sum of points won
total_puzzle1_points = sum([puzzle1(x, y) for [x, y] in input])
print(total_puzzle1_points)

# Puzzle 2
total_puzzle2_points = sum([puzzle2(x, y) for [x, y] in input])
print(total_puzzle2_points)
