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

# Part 1
data = []
for line in store:
    data.append([x for x in line])
# Convert to DataFrame
import pandas as pd
df = pd.DataFrame(data)
# print(df)
num = 0
for row in df.iterrows():
    row_string = ''.join(row[1].values)
    num += row_string.count("XMAS")
    row_string_rev = row_string[::-1]
    num += row_string_rev.count("XMAS")
    # print(row_string, row_string_rev, row_string.count("XMAS"), row_string_rev.count("XMAS"))
for column_name, column_data in df.items():
    column_string = ''.join(column_data.values)
    num += column_string.count("XMAS")
    column_string_rev = column_string[::-1]
    num += column_string_rev.count("XMAS")
    # print(column_string, column_string_rev, column_string.count("XMAS"), column_string_rev.count("XMAS"))
# Do diagonals
# Function to get all diagonals from the DataFrame
def get_diagonals(df):
    diagonals = []
    rows, cols = df.shape
    # Get all diagonals from top-left to bottom-right
    for diag in range(rows + cols - 1):
        diagonal = []
        for row in range(max(0, diag - cols + 1), min(rows, diag + 1)):
            col = diag - row
            diagonal.append(df.iat[row, col])
        diagonals.append(diagonal)
        diagonals.append(diagonal[::-1])
    # Get all diagonals from top-right to bottom-left
    for diag in range(rows + cols - 1):
        diagonal = []
        for row in range(max(0, diag - cols + 1), min(rows, diag + 1)):
            col = cols - 1 - (diag - row)
            diagonal.append(df.iat[row, col])
        diagonals.append(diagonal)
        diagonals.append(diagonal[::-1])
    return diagonals
diagonals = get_diagonals(df)
for diag in diagonals:
    num += ''.join(diag).count("XMAS")
# print(num)

# Part 2
# Attempt a convulutional search?
# Function to extract 3x3 sub-DataFrames
def extract_sub_dataframes(df, size=3):
    sub_dataframes = []
    rows, cols = df.shape
    for i in range(rows - size + 1):
        for j in range(cols - size + 1):
            sub_df = df.iloc[i:i+size, j:j+size]
            sub_dataframes.append(sub_df)
    return sub_dataframes
# Extract 3x3 sub-DataFrames
sub_dataframes = extract_sub_dataframes(df)
sample_data = [
    ['M', '.', 'S'],
    ['.', 'A', '.'],
    ['M', '.', 'S']
]
sample = pd.DataFrame(sample_data)
# Example usage: print all 3x3 sub-DataFrames
num = 0
for sub_df in sub_dataframes:
    # print(sub_df)
    pass

    # Check for 
    # M.S
    # .A.
    # M.S
    is_correct = sub_df.iat[0,0] == "M" and sub_df.iat[0,2] == "S" and sub_df.iat[2,0] == "M" and sub_df.iat[2,2] == "S" and sub_df.iat[1,1] == "A"
    if is_correct:
        # print("Matched")
        num += 1    
    
    # Check for 
    # M.M
    # .A.
    # S.S
    is_correct = sub_df.iat[0,0] == "M" and sub_df.iat[0,2] == "M" and sub_df.iat[2,0] == "S" and sub_df.iat[2,2] == "S" and sub_df.iat[1,1] == "A"
    if is_correct:
        # print("Matched")
        num += 1
    
    # Check for 
    # S.M
    # .A.
    # S.M
    is_correct = sub_df.iat[0,0] == "S" and sub_df.iat[0,2] == "M" and sub_df.iat[2,0] == "S" and sub_df.iat[2,2] == "M" and sub_df.iat[1,1] == "A"
    if is_correct:
        # print("Matched")
        num += 1
    
    # Check for 
    # S.S
    # .A.
    # M.M
    is_correct = sub_df.iat[0,0] == "S" and sub_df.iat[0,2] == "S" and sub_df.iat[2,0] == "M" and sub_df.iat[2,2] == "M" and sub_df.iat[1,1] == "A"
    if is_correct:
        # print("Matched")
        num += 1

    # print()

print(num)
