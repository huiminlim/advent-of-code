from collections import defaultdict
import os

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#print(ROOT_DIR)

# Parse input strings
store = []
with open(f"{ROOT_DIR}/data.txt", "r") as f:
    for line in f:
        store.append(line.strip())

# Solve Part 1
score = 0
for line in store:
    card = line.split(":")[-1].strip().split("|")
    winning = [int(x) for x in card[0].strip().split(" ") if x != ""]
    match = [int(x) for x in card[1].strip().split(" ") if x != ""]
    count = 0
    for num in winning:
        if num in match:
            count += 1
    if count > 0:
        score += 2 ** (count - 1)

# print(score)

# Solve Part 2
total_num_cards = len(store)
cards = defaultdict()
for i in range(1, len(store)+1):
    cards.setdefault(i, 1)
card_id = 1
for line in store:
    for _ in range(cards[card_id]):
        card = line.split(":")[-1].strip().split("|")
        winning = [int(x) for x in card[0].strip().split(" ") if x != ""]
        match = [int(x) for x in card[1].strip().split(" ") if x != ""]
        count = 0
        for num in winning:
            if num in match:
                count += 1
        if count > 0:
            for idx in range(card_id+1, card_id+count+1):
                if idx <= total_num_cards:
                    cards[idx] += 1
    # print(cards)
    card_id += 1

total_cards = 0
for num_cards in cards.values():
    total_cards += num_cards
print(total_cards)
