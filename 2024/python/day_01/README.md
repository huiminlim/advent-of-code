# AoC 2024 Day 1

In Part 2, I chanced upon the `collections.Counter` library (read [here](https://www.adventuresinmachinelearning.com/maximizing-python-efficiency-counting-and-multisets-with-counter/) when I wanted to count the number of times the first value occurs in the second list.

I read about people [comparing the efficiency](https://stackoverflow.com/questions/41594940/why-is-collections-counter-so-slow) in solving similar problems, like [counting nucleotides in DNA](https://rosalind.info/problems/dna/)

I found out that `collections.Counter` is implemented in Python and it is quite fast for Python basic items. For string operations, Strings are implemented in C wrappers and to sort string/characters, the `String` library is more optimized for that purpose.

The breakeven comes when multiple loops are used when comparing `Strings`, whereas `collections.Counter` only traverses the loop once.

![Chart](https://i.sstatic.net/LqqBs.png)
