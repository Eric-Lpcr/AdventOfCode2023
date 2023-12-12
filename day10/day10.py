import logging

from utilities.coordinates import Coordinate2

NORTH, EAST, SOUTH, WEST = Coordinate2(0, -1), Coordinate2(1, 0), Coordinate2(0, 1), Coordinate2(-1, 0)

GROUND = '.'
ANIMAL = 'S'
VERTICAL_PIPE = '|'
HORIZONTAL_PIPE = '-'
SOUTH_WEST_PIPE = 'L'
SOUTH_EAST_PIPE = 'J'
NORTH_EAST_PIPE = '7'
NORTH_WEST_PIPE = 'F'

PIPES = {  # pipe: {from_direction: to_direction, ...}
    VERTICAL_PIPE: {NORTH: NORTH, SOUTH: SOUTH},
    HORIZONTAL_PIPE: {EAST: EAST, WEST: WEST},
    SOUTH_WEST_PIPE: {SOUTH: EAST, WEST: NORTH},
    SOUTH_EAST_PIPE: {SOUTH: WEST, EAST: NORTH},
    NORTH_EAST_PIPE: {NORTH: WEST, EAST: SOUTH},
    NORTH_WEST_PIPE: {NORTH: EAST, WEST: SOUTH},
    ANIMAL: {},
    GROUND: {}
}


def find_animal(maze):
    for y, line in enumerate(maze):
        if ANIMAL in line:
            x = line.index(ANIMAL)
            return Coordinate2(x, y)


def at(position: Coordinate2, maze):
    return maze[position.y][position.x]


def find_loop(maze):
    start_position = find_animal(maze)
    pipe_loop = [start_position]

    for direction in (NORTH, EAST, SOUTH, WEST):  # explore neighbors
        next_pipe = at(start_position + direction, maze)
        if direction in PIPES[next_pipe]:  # can enter pipe in this direction, first one is chosen
            break

    position = start_position
    while True:
        position += direction
        pipe_loop.append(position)
        pipe = at(position, maze)
        if pipe == ANIMAL:
            break
        direction = PIPES[pipe].get(direction)
        if direction is None:
            raise ValueError('Cannot go through this pipe')

    return pipe_loop


def compute_start_pipe(maze, start_position):
    start_directions = []
    for direction in (NORTH, EAST, SOUTH, WEST):
        pipe = at(start_position + direction, maze)
        if direction in PIPES[pipe]:
            start_directions.append(direction)

    for pipe, moves in PIPES.items():
        pipe_directions = moves.keys()
        if all(start_direction in pipe_directions for start_direction in start_directions):
            return pipe


def ray_crosses(ray):
    crosses = 0
    previous_angle = None
    for tile in ray:
        if tile != GROUND:
            if tile == VERTICAL_PIPE:
                crosses += 1
                previous_angle = None
            elif tile in (NORTH_WEST_PIPE, SOUTH_WEST_PIPE):  # left angle, opening
                previous_angle = tile
            elif tile in (NORTH_EAST_PIPE, SOUTH_EAST_PIPE):  # right angle, closing
                if previous_angle:
                    if ((previous_angle == SOUTH_WEST_PIPE and tile == NORTH_EAST_PIPE)  # L...7 => crossing
                            or (previous_angle == NORTH_WEST_PIPE and tile == SOUTH_EAST_PIPE)):  # F...J
                        crosses += 1
                    else:  # L...J or F...7 => no crossing
                        pass
                previous_angle = None
    return crosses


def build_loop_map(maze, pipe_loop):
    """Returns a matrix with only pipe elements"""
    loop_map = [[GROUND] * len(maze[0]) for _ in range(len(maze))]
    for position in pipe_loop:
        loop_map[position.y][position.x] = at(position, maze)
    start_position = pipe_loop[0]
    loop_map[start_position.y][start_position.x] = compute_start_pipe(maze, start_position)
    return loop_map


def nest_area(maze, pipe_loop):
    loop_map = build_loop_map(maze, pipe_loop)
    area = 0
    for y in range(len(loop_map)):
        for x in range(len(loop_map[0])):
            if loop_map[y][x] == GROUND:
                crosses = ray_crosses(loop_map[y][:x])
                if crosses % 2 == 1:  # odd number of ray / pipe crossings => inside
                    area += 1
                    loop_map[y][x] = '*'

    logging.debug('\n'.join(''.join(line) for line in loop_map))
    return area


def solve_problem(filename, expected1=None, expected2=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        maze = [line.strip() for line in f.readlines()]

    pipe_loop = find_loop(maze)

    result1 = len(pipe_loop) // 2
    print(f"Part 1: farthest position in loop is {result1}")
    if expected1 is not None:
        assert result1 == expected1

    result2 = nest_area(maze, pipe_loop)
    print(f"Part 2: nest area is {result2}")
    if expected2 is not None:
        assert result2 == expected2


def main():
    solve_problem('test.txt', 4, 1)
    solve_problem('test2.txt', 8, 0)
    solve_problem('test3.txt', 80, 10)
    solve_problem('input.txt', 7145, 445)


if __name__ == '__main__':
    main()
