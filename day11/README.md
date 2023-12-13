# [Day 11: Cosmic Expansion](https://adventofcode.com/2023/day/11)

Couldn't resist to use numpy... 

## Part 1
Read the image in a matrix of zeroes (empty) and ones (galaxy).

Basic and stupid implementation: expand lines and columns according to galaxy in order to build an expanded image
in universe coordinates.

Used `np.hstack` and `np.vstack`, `ndarray.any` to detect galaxies on lines and columns.

Galaxies are found in the image with `np.where` which gives two vectors of coordinates to be reassembled with `zip`
in a `Coordinate2` array.

Compute manhattan distances on all possible pairs using `itertools.combinations`.

## Part 2
Gosh, I should have realised that expansion factor would increase...

Good way of doing things: establish a correspondence (scale) between image coordinates and universe coordinates.

Computes the real width of all columns and rows with `np.apply_along_axis`, then cumulatively add them with `np.cumsum`
to get the x and y scales. 
Then transform galaxies image coordinates to universe coordinates before computing distances.
