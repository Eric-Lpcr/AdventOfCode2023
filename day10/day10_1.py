from utilities.coordinates import Coordinate2

NORTH, EAST, SOUTH, WEST = Coordinate2(0, -1), Coordinate2(1, 0), Coordinate2(0, 1), Coordinate2(-1, 0)

PIPES = {  # pipe: {from_direction: to_direction, ...}
    '|': {NORTH: NORTH, SOUTH: SOUTH},
    '-': {EAST: EAST, WEST: WEST},
    'L': {SOUTH: EAST, WEST: NORTH},
    'J': {SOUTH: WEST, EAST: NORTH},
    '7': {NORTH: WEST, EAST: SOUTH},
    'F': {NORTH: EAST, WEST: SOUTH},
    'S': {},
    '.': {}
}

ANIMAL = 'S'


def find_animal(maze):
    for y, line in enumerate(maze):
        if ANIMAL in line:
            x = line.index(ANIMAL)
            return Coordinate2(x, y)


def at(position: Coordinate2, maze):
    return maze[position.y][position.x]


def loop_size(maze):
    steps = 0
    start_position = find_animal(maze)

    for direction in (NORTH, EAST, SOUTH, WEST):  # explore neighbors
        next_pipe = at(start_position + direction, maze)
        if direction in PIPES[next_pipe]:  # can enter pipe in this direction, first one is chosen
            break

    position = start_position
    while True:
        position += direction
        steps += 1
        pipe = at(position, maze)
        if pipe == ANIMAL:
            break
        direction = PIPES[pipe].get(direction)
        if direction is None:
            raise ValueError('Cannot go through this pipe')

    return steps


def solve_problem(filename, expected1=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        maze = [line.strip() for line in f.readlines()]

    result1 = loop_size(maze) // 2
    print(f"Part 1: farthest position in loop is {result1}")
    if expected1 is not None:
        assert result1 == expected1


def main():
    solve_problem('test.txt', 4)
    solve_problem('test2.txt', 8)
    solve_problem('input.txt', 7145)


if __name__ == '__main__':
    main()
