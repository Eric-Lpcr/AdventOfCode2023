# [Day 2: Cube Conundrum](https://adventofcode.com/2023/day/2)

Decoding text and using collection iteration functions.

## Part 1
Used `split` to cut the game set string in pieces and set up a small GameSet class.
Added a method to compare a game set with a bag (which is a game set).

Same class for a game and all its game sets.

Filter game sets with a for-in-if comprehension list.

## Part 2
Added some methods to compute minimum bag and power.
Used `@property` annotation for methods without parameters.

Needed a list() in front of map to keep it for part 2. Removed map for a comprehension list.
