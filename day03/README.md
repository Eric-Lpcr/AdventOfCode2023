# [Day 3: Gear Ratios](https://adventofcode.com/2023/day/3)

String slicing.

## Part 1
Added a border of dots to manage indices out of input data range.
Iteration over numbers with a regex and `re.finditer`, and scan neighboring with slicing.

Got problems with end of lines that I forgot to remove...

## Part 2
Instead of finding generic symbols (nor a digit, nor a dot), find explicitely a gear symbol. Memoize it in a dictionary
with a position key (line and column tuple) and a value giving the list of adjacent part numbers. 
Used `defaultdict` to initialise the list value on insertion.
