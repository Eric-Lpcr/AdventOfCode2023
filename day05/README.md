# [Day 5: If You Give A Seed A Fertilizer](https://adventofcode.com/2023/day/5)

Data transformation.

## Part 1
Built a structure of callable mappers to handle all the plan. Just need to execute the plan on each seed to get the
locations and compute the minimal one.

## Part 2
Wow, day 5 and already complexity problem. Brute force can't work, even with input data simplification attempt.

Thought about a trick which consisted on reverse processing, but the problem doesn't seem compatible.

Ok, let's go for range arithmetics. The point is about slicing the input ranges according to mapping ranges in order to
apply the transformation on right places.

Took a bit to set it working, but like often in Python, once some few points corrected, it works on test data and... 
suspense... on input data too! 

# Capitalisation
in [utilities/range.py](../utilities/range.py)

## `Range` 
A class with more interval operations than built-in `range`. 

Especially the `cut` method which cuts the current range in pieces according to another range. 

For example:

    Range(0, 10).cut(Range(5, 7))

gives a `MultiRange` with value [0, 5[ U [5, 7[ U [7, 10[

## `MultiRange` 
A class to handle a union of `Range`.