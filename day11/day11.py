import numpy as np
from itertools import combinations
from utilities.coordinates import Coordinate2

GALAXY = '#'


def galaxy_distances(image, expansion_factor):
    def scale(arr):
        return 1.0 if arr.any() else float(expansion_factor)

    x_scale = np.cumsum(np.apply_along_axis(scale, 1, image))  # real universe coordinates
    y_scale = np.cumsum(np.apply_along_axis(scale, 0, image))

    galaxy_coordinates = [Coordinate2(x_scale[x], y_scale[y]) for x, y in zip(* np.where(image))]
    distances = [c1.manhattan_to(c2) for c1, c2 in combinations(galaxy_coordinates, 2)]
    return distances


def solve_problem(filename, expected1=None, expected2=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        image = np.array([list(line.strip()) for line in f.readlines()]) == GALAXY

    distances = galaxy_distances(image, expansion_factor=2)
    result1 = int(sum(distances))
    print(f"Part 1: sum of lengths is {result1}")
    if expected1 is not None:
        assert result1 == expected1

    distances = galaxy_distances(image, expansion_factor=1e6)
    result2 = int(sum(distances))
    print(f"Part 2: sum of lengths is {result2}")
    if expected2 is not None:
        assert result2 == expected2


def main():
    solve_problem('test.txt', 374, 82000210)
    solve_problem('input.txt', 9445168, 742305960572)


if __name__ == '__main__':
    main()
