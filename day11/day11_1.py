from itertools import combinations

import numpy as np
from utilities.coordinates import Coordinate2

GALAXY = '#'


def expand_universe(image):
    rows, cols = image.shape
    row_expanded_image = np.empty((0, cols))
    for row_index in range(rows):
        new_row = image[[row_index], :]
        row_expanded_image = np.vstack((row_expanded_image, new_row))
        if not new_row.any():
            row_expanded_image = np.vstack((row_expanded_image, new_row))

    rows, cols = row_expanded_image.shape
    expanded_image = np.empty((rows, 0))
    for col_index in range(cols):
        new_col = row_expanded_image[:, [col_index]]
        expanded_image = np.hstack((expanded_image, new_col))
        if not new_col.any():
            expanded_image = np.hstack((expanded_image, new_col))

    return expanded_image


def galaxy_distances(image):
    galaxy_coordinates = [Coordinate2(x, y) for x, y in zip(* np.where(image))]
    distances = [c1.manhattan_to(c2) for c1, c2 in combinations(galaxy_coordinates, 2)]
    return distances


def solve_problem(filename, expected1=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        image = np.array([list(line.strip()) for line in f.readlines()]) == GALAXY

    expanded_image = expand_universe(image)
    distances = galaxy_distances(expanded_image)

    result1 = sum(distances)
    print(f"Part 1: sum of lengths is {result1}")
    if expected1 is not None:
        assert result1 == expected1


def main():
    solve_problem('test.txt', 374)
    solve_problem('input.txt', 9445168)


if __name__ == '__main__':
    main()
