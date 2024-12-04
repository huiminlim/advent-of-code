# AoC 2023 Day 3

I expanded the grid to add padding to make searching the boundary of each original pixel easier.

For example, the character `X` is added.

```
XXXXXXXXXXXX
X467..114..X
X...*......X
X..35..633.X
X......#...X
X617*......X
X.....+.58.X
X..592.....X
X......755.X
X...$.*....X
X.664.598..X
XXXXXXXXXXXX
```

## Part 1

I checked the following values if applicable:

1. Left number
2. Right number
3. Top number
4. Bottom number
5. Diagonal numbers, if the top/bottom character is a `.`

## Part 2

This was similar to part 1, but I multiplied them instead after finding the numbers to derive the gear ratio.
