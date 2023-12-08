# [Day 7: Camel Cards](https://adventofcode.com/2023/day/7)

Comparison and sort.

## Part 1
Need to sort hands according to type (Five in a hand, Full house...) criteria, then card value if type is same.

Hand types strength are enumerated with an `IntEnum` which is sortable.
Detection of hand type is made with a double `Counter` which gives the number of sets of identical cards.

Card comparison is made by a simple string comparison, after translating figures characters to alphabetically ordered 
characters. No need to translate digits as they are already ordered and are lower than letters.

## Part 2
Jokers change the ordering on the two criteria.

Hand type is first computed with all cards except jokers. 
The jokers are counted and a dictionary gives the final hand type according to the type got with classic cards
and the number of jokers.

Put back the digits in a supplementary translation table to have the joker at the lowest strength.