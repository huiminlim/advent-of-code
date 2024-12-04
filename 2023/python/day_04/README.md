# AoC 2023 Day 4

## Part 1

This part was relatively easy after parsing the numbers from the winning numbers and the match numbers set.

I searched if the count which the numbers in the winning numbers appeared in the match set and computed the score using by raising to the power of 2 less 1.

## Part 2

Relatively similar to Part 1. But this time, I keep a dictionary count of the number of cards amassed for each card id after each round.

After finishing the entire pass, I summed the number of cards amassed in the dictionary.
