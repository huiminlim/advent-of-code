# AoC 2023 Day 1

## Part 1

Figured out the first part rather quickly by searching front and backwards for digits, then breaking.

## Part 2

Initially I thought I could search each substring that begins with each character in the string and replace it with the corresponding digit if it matches the word.

But it fails on the case `eightwothree`, as I didn't realize it should resolve to `823`, rather than `8wo3`.

Searched Reddit and realized that it should be replaced with the last character and first character intact.
