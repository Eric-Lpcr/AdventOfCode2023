# [Day 8: Haunted Wasteland](https://adventofcode.com/2023/day/8)

Navigation.

## Part 1
Built a generator function to iterate over instructions with `cycle`.

## Part 2
Ok for test data with a simple iteration. But don't finish on problem input, going to millions of iterations.

Thought about a previous problem with such alignment of things, solution was about detecting cycles. 
Must be that here, having millions of instructions with 269 instructions and 776 nodes.

I tried to explore the dataset, detecting cycles (entering same node with same instruction index).

I improved the generator to give the step (total iteration) and the instruction number (reset to 0 at each cycle).
Gave me a nice `enumerate(cycle(enumerate(...)))`

Found strange things with 'Z' end detected before the repetition at the same number of steps than the repetition 
restart. 

Took these numbers and computed the least common multiplier... And it was luckily the answer.
First not so simple problem!

