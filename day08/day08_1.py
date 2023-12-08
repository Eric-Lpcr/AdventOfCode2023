from itertools import cycle

LEFT, RIGHT = 0, 1


def directions(instructions):
    yield from cycle(list(LEFT if instruction == 'L' else RIGHT for instruction in instructions))


def navigate(network, instructions, start='AAA', destination='ZZZ'):
    steps = 0
    place = start
    direction = directions(instructions)
    while place != destination:
        place = network[place][next(direction)]
        steps += 1
    return steps


def solve_problem(filename, expected1=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        def decode_line(line):
            place, left, right = line.replace('= (', '').replace(',', '').replace(')', '').split()
            return place, (left, right)

        instructions = f.readline().strip()
        f.readline()
        network = dict(map(decode_line, f.readlines()))

    result1 = navigate(network, instructions)
    print(f"Part 1: number of steps is {result1}")
    if expected1 is not None:
        assert result1 == expected1


def main():
    solve_problem('test.txt', 2)
    solve_problem('test2.txt', 6)
    solve_problem('input.txt', 19099)


if __name__ == '__main__':
    main()
