# [Day 10: Pipe Maze](https://adventofcode.com/2023/day/10)


## Part 1
Set up some constants to describe the rules, mainly the direction change on each kind of pipe element.

Need to find the start position, and a direction to go first, with a compatible pipe element.
Then it's a trivial exploration by following the directions and detecting the return to the start. 

At least there's no three-way part which would need backtracking!

## Part 2
Part 1 gives the loop. Just need to deduce the pipe element which takes place at the start.

Used a maze map with only loop pipe, and traced a left to right ray to count the crossings to each free position.
If the number of crossings is odd, then the position is inside the loop, in the nest area.

Had to manage special cases with successive turn pipes which can be considered both as a crossing or not:

* `L...7` and `F...J` are crossed, they form a vertical line (North <-> South).
* `L...J` and `F...7` are not crossed as they form an edge (South <-> South or North <-> North) 
which lets a succeeding position outside.

## Reuse
`Coordinate2` from last year.