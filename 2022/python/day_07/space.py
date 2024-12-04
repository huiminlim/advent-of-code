import os
import re

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

cmds = []
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    for line in f:
        cmds.append(line.strip().replace("$ ", ""))

current_dir = []
sizes = {}
has_sizes = re.compile(r"^\d.")
for cmd in cmds:
    if "cd" in cmd:
        dir = cmd.split()[1]

        if dir == "..":
            current_dir = current_dir[:-1]
        else:
            current_dir.append(dir)

        pwd = "/".join(current_dir)[1:]

        if pwd not in sizes.keys():
            sizes[pwd] = 0

    elif re.match(has_sizes, cmd):
        size = cmd.split(" ")[0]

        pwd = "/".join(current_dir)[1:]
        sizes[pwd] = sizes[pwd] + int(size)

print(f"sizes: {sizes}")

# Compute the size of a directory and all the subdirectory
computed_sizes = {}
for abspath in sizes.keys():
    computed_sizes[abspath] = sizes[abspath]

    # Find the subdirectories
    for other in sizes.keys():
        if other != abspath and other.startswith(abspath):
            computed_sizes[abspath] = computed_sizes[abspath] + sizes[other]

    print(computed_sizes)

total_size = 0
for abspath, size in computed_sizes.items():
    if size <= 100000:
        total_size += size

print(total_size)
