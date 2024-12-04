# AoC 2023 Day 2

## Part 1

This part was rather easy after parsing and organizing each game info.

I parsed each set on every line to a dictionary of cube counts, e.g. `{"red": 1, "blue": 3, "green": 3}`, then checked if any of them exceeded the required limits.

## Part 2

This part was also relatively straightforward, similar to Part 1.

After parsing, instead of checking if a hard limit was passed, I checked for the upper bound of possible cubes.
