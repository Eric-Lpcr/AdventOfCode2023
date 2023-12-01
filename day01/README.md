# [Day 1: Trebuchet?!](https://adventofcode.com/2023/day/1)

Warm up about splitting files and lines, lists, filtering, sum ... and finally regular expressions.

## Part 1
Single character problem solved by transforming each line to a list and filtering digits. Getting first and last digit
is a matter of indexing.

## Part 2
Sub chain search with text figures. Used a RE computed from a constant dictionary of figures (text and digits) giving
value.

First digit is easy to find with a `re.search`. 

Thought about a more complex (greedy) RE to match both first and last, but it can be the same...

Thought also to use `re.find_all` to find all figures and keep first and last like in part 1, but this won't work on
overlapping figures (like 'nineight'). This point was not in the problem description, but would be difficult to debug
if present in the input.

My trick here is to search from the end by reversing both the line and the pattern (looking for 'eno' instead of 'one'). 
BTW it's quite strange that there is no built-in function te revert a string...

## Further work
Looked for an 'last match' regular expression and find `'(?s:.*)pattern'`.

https://stackoverflow.com/questions/33232729/how-to-search-for-the-last-occurrence-of-a-regular-expression-in-a-string-in-pyt

And put all constant in a class to avoid globals.
