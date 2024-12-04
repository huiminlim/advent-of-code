import os

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# print(ROOT_DIR)

# Parse input strings
store = []
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    for line in f:
        store.append(line.strip())
ncol = len(store[0])
nrow = len(store)

# Pretty print maze
def print_maze(maze):
    for line in maze:
        print(line)

# Expand the maze board
maze = []
maze.append("." * (ncol + 2))
for line in store:
    maze.append("." + line + ".")
maze.append("." * (ncol + 2))
# print_maze(maze)
# print(f"Dims (r, c): {len(maze)} {len(maze[0])}")

# Part 1: Brute force check the maze map
total_val = 0
for r in range(1, len(maze)-1):
    for c in range(1, len(maze[r])-1):
        # Check if it is a symbol
        char = maze[r][c]
        if not char.isdigit() and char != ".":
            # Search right numbers
            right_num = 0
            if maze[r][c+1].isdigit():
                for idx in range(c+1, len(maze[r])):
                    if maze[r][idx].isdigit():
                        right_num = int(maze[r][c+1:idx+1])
                    else:
                        break
                # print(right_num)
            total_val += right_num

            # Search left number
            left_num = 0
            substr = maze[r][:c]
            tokens = substr.split(".")
            if len(tokens) != 0 and tokens[-1].isdigit():
                left_num = int(tokens[-1])
                total_val += left_num

            # Search top number
            top_num = 0
            if maze[r-1][c].isdigit():
                start_idx = c
                end_idx = c
                while start_idx >= 0:
                    if maze[r-1][start_idx].isdigit():
                        start_idx -= 1
                    else:
                        break
                start_idx += 1
                while end_idx < len(maze[r]):
                    if maze[r-1][end_idx].isdigit():
                        end_idx += 1
                    else:
                        break
                top_num = int(maze[r-1][start_idx:end_idx])
                total_val += top_num

            # Search bottom number
            bottom_num = 0
            if maze[r+1][c].isdigit():
                start_idx = c
                end_idx = c
                while start_idx >= 0:
                    if maze[r+1][start_idx].isdigit():
                        start_idx -= 1
                    else:
                        break
                start_idx += 1
                while end_idx < len(maze[r]):
                    if maze[r+1][end_idx].isdigit():
                        end_idx += 1
                    else:
                        break
                bottom_num = int(maze[r+1][start_idx:end_idx])
                total_val += bottom_num

            # Search diagonal left up
            diag_left_up_num = 0
            if maze[r-1][c-1].isdigit() and maze[r-1][c] == ".":
                start_idx = c-1
                end_idx = c-1
                while start_idx >= 0:
                    if maze[r-1][start_idx].isdigit():
                        start_idx -= 1
                    else:
                        break
                start_idx += 1
                while end_idx <= c-1:
                    if maze[r-1][end_idx].isdigit():
                        end_idx += 1
                    else:
                        break
                diag_left_up_num = int(maze[r-1][start_idx:end_idx])
                total_val += diag_left_up_num

            # Search diagonal left down
            diag_left_down_num = 0
            if maze[r+1][c-1].isdigit() and maze[r+1][c] == ".":
                start_idx = c-1
                end_idx = c-1
                while start_idx >= 0:
                    if maze[r+1][start_idx].isdigit():
                        start_idx -= 1
                    else:
                        break
                start_idx += 1
                while end_idx <= c-1:
                    if maze[r+1][end_idx].isdigit():
                        end_idx += 1
                    else:
                        break
                diag_left_down_num = int(maze[r+1][start_idx:end_idx])
                total_val += diag_left_down_num

            # Search diagonal right up
            diag_right_up_num = 0
            if maze[r-1][c+1].isdigit() and maze[r-1][c] == ".":
                start_idx = c+1
                end_idx = c+1
                while end_idx <= len(maze[r]):
                    if maze[r-1][end_idx].isdigit():
                        end_idx += 1
                    else:
                        break
                diag_right_up_num = int(maze[r-1][start_idx:end_idx])
                total_val += diag_right_up_num

            # Search diagonal right down
            diag_right_down_num = 0
            if maze[r+1][c+1].isdigit() and maze[r+1][c] == ".":
                start_idx = c+1
                end_idx = c+1
                while end_idx <= len(maze[r]):
                    if maze[r+1][end_idx].isdigit():
                        end_idx += 1
                    else:
                        break
                diag_right_down_num = int(maze[r+1][start_idx:end_idx])
                total_val += diag_right_down_num

# print(total_val)


# Part 2
total_val = 0
for r in range(1, len(maze)-1):
    for c in range(1, len(maze[r])-1):
        # Check if it is a symbol
        char = maze[r][c]
        if char == "*":
            vals = []

            top_char = maze[r-1][c]
            if top_char == ".": # search diagonal left and right only
                if maze[r-1][c-1].isdigit():
                    start_idx = c-1
                    end_idx = c-1
                    while start_idx >= 0:
                        if maze[r-1][start_idx].isdigit():
                            start_idx -= 1
                        else:
                            break
                    start_idx += 1
                    while end_idx <= c-1:
                        if maze[r-1][end_idx].isdigit():
                            end_idx += 1
                        else:
                            break
                    diag_left_up_num = int(maze[r-1][start_idx:end_idx])
                    vals.append(diag_left_up_num)
                if maze[r-1][c+1].isdigit():
                    diag_right_up_num = 0
                    if maze[r-1][c+1].isdigit() and maze[r-1][c] == ".":
                        start_idx = c+1
                        end_idx = c+1
                        while end_idx <= len(maze[r]):
                            if maze[r-1][end_idx].isdigit():
                                end_idx += 1
                            else:
                                break
                        diag_right_up_num = int(maze[r-1][start_idx:end_idx])
                        vals.append(diag_right_up_num)
            else: # expand the number by searching left and right of this char
                if top_char.isdigit():
                    left_idx = c
                    right_idx = c
                    while left_idx >= 0:
                        if maze[r-1][left_idx-1].isdigit():
                            left_idx -= 1
                        else:
                            break
                    while right_idx < len(maze[r]):
                        if maze[r-1][right_idx+1].isdigit():
                            right_idx += 1
                        else:
                            break
                    vals.append(int(maze[r-1][left_idx: right_idx+1]))

            bottom_char = maze[r+1][c]
            if bottom_char == ".": # search diagonal only
                if maze[r+1][c-1].isdigit():
                    diag_left_down_num = 0
                    if maze[r+1][c-1].isdigit() and maze[r+1][c] == ".":
                        start_idx = c-1
                        end_idx = c-1
                        while start_idx >= 0:
                            if maze[r+1][start_idx].isdigit():
                                start_idx -= 1
                            else:
                                break
                        start_idx += 1
                        while end_idx <= c-1:
                            if maze[r+1][end_idx].isdigit():
                                end_idx += 1
                            else:
                                break
                        diag_left_down_num = int(maze[r+1][start_idx:end_idx])
                        vals.append(diag_left_down_num)
                if maze[r+1][c+1].isdigit():
                    diag_right_down_num = 0
                    if maze[r+1][c+1].isdigit() and maze[r+1][c] == ".":
                        start_idx = c+1
                        end_idx = c+1
                        while end_idx <= len(maze[r]):
                            if maze[r+1][end_idx].isdigit():
                                end_idx += 1
                            else:
                                break
                        diag_right_down_num = int(maze[r+1][start_idx:end_idx])
                        vals.append(diag_right_down_num)
            else: # expand the number by searching left and right of this char
                if bottom_char.isdigit():
                    left_idx = c
                    right_idx = c
                    while left_idx >= 0:
                        if maze[r+1][left_idx-1].isdigit():
                            left_idx -= 1
                        else:
                            break
                    while right_idx < len(maze[r]):
                        if maze[r+1][right_idx+1].isdigit():
                            right_idx += 1
                        else:
                            break
                    vals.append(int(maze[r+1][left_idx: right_idx+1]))

            left_char = maze[r][c-1]
            if left_char.isdigit():
                # Search left number
                left_num = 0
                substr = maze[r][:c]
                tokens = substr.split(".")
                if len(tokens) != 0 and tokens[-1].isdigit():
                    left_num = int(tokens[-1])
                    vals.append(left_num)

            right_char = maze[r][c+1]
            if right_char.isdigit():
                # Search right numbers
                right_num = 0
                if maze[r][c+1].isdigit():
                    for idx in range(c+1, len(maze[r])):
                        if maze[r][idx].isdigit():
                            right_num = int(maze[r][c+1:idx+1])
                        else:
                            break
                vals.append(right_num)

            if len(vals) == 2:
                total_val += vals[0] * vals[1]

print(total_val)
