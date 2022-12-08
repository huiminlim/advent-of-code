import os

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

grid = []
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    for line in f:
        grid.append([x for x in line.strip()])

nrow = len(grid)
ncol = len(grid[0])


def is_visible(height: int, slice: list) -> bool:
    if len(slice) == 0:
        return True
    return all([x < height for x in slice])


# Puzzle 1
total_visible = 0
for y in range(nrow):
    for x in range(ncol):

        height = grid[y][x]

        left_slice = grid[y][:x]
        right_slice = grid[y][x + 1:]
        bottom_slice = [row[x] for row in grid][y + 1:]
        up_slice = [row[x] for row in grid][:y]

        left_visible = is_visible(height, left_slice)
        right_visible = is_visible(height, right_slice)
        bottom_visible = is_visible(height, bottom_slice)
        up_visible = is_visible(height, up_slice)

        visible = False
        if (x == 0 or y == 0 or x == ncol - 1 or y == nrow - 1) or left_visible or right_visible or bottom_visible or up_visible:
            total_visible += 1
            visible = True

    #     print(left_slice, right_slice, up_slice, bottom_slice, height, visible)
    # print()

print(total_visible)
