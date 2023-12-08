# [Day 6: Wait For It](https://adventofcode.com/2023/day/6)


## Part 1
Naive iteration on possible button hold time. Distance is given by speed (hold time) multiplied by remaining time.
Just filtered the results giving a better distance.

## Part 2
Noted that distance is the result of a second degree polynom. 

    distance = speed x (time - hold_time)
    speed = hold_time
    distance > record => distance - record > 0 
    
    -hold_time^2 + time x hold_time - record > 0

First coefficient is negative so polynom is positive between roots given by 
[quadratic formula](https://en.wikipedia.org/wiki/Quadratic_formula).
Just need to count the integers between roots.
