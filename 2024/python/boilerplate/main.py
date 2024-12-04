import os

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#print(ROOT_DIR)

# Data file name
# data_file = "test_data.txt"
data_file = "data.txt"

# Parse input strings
store = []
with open(f"{ROOT_DIR}/{data_file}", "r") as f:
    for line in f:
        store.append(line.strip())
