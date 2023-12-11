from itertools import cycle
from math import lcm

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


def navigate2(network, instructions):
    steps = 0
    places = [place for place in network if place[2] == 'A']
    direction = directions(instructions)
    while any(map(lambda place: place[2] != 'Z', places)):
        next_direction = next(direction)
        places = [network[place][next_direction] for place in places]
        steps += 1
        if steps % 1000 == 0:
            print(steps)
    return steps


def directions_with_indices(instructions):
    yield from enumerate(cycle(enumerate(list(LEFT if instruction == 'L' else RIGHT for instruction in instructions))))


def explore(network, instructions):
    places = [place for place in network if place[2] == 'A']
    for place in places:
        print("Start", place)
        visited = dict()
        for step, (instruction_index, next_direction) in directions_with_indices(instructions):
            if (place, instruction_index) in visited:
                print("    Repeat at", step, place, instruction_index)
                break
            if place.endswith('Z'):
                print("    Z reached", step, place, instruction_index)
            visited[(place, instruction_index)] = step
            place = network[place][next_direction]


def navigate3(network, instructions):
    steps = []
    starts = [place for place in network if place.endswith('A')]
    for place in starts:
        for step, (instruction_index, next_direction) in directions_with_indices(instructions):
            if place.endswith('Z'):
                steps.append(step)
                break
            place = network[place][next_direction]
    print('Loops:', steps)
    return lcm(*steps)


def solve_problem(filename, expected1=None, expected2=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        def decode_line(line):
            place, left, right = line.replace('= (', '').replace(',', '').replace(')', '').split()
            return place, (left, right)

        instructions = f.readline().strip()
        f.readline()
        network = dict(map(decode_line, f.readlines()))

    if expected1 is not None:
        result1 = navigate(network, instructions)
        print(f'Part 1: number of steps is {result1}')
        assert result1 == expected1

    if expected2 is not None:
        explore(network, instructions)
        result2 = navigate3(network, instructions)
        print(f'Part 2: number of steps is {result2}')
        assert result2 == expected2


def main():
    solve_problem('test.txt', 2, None)
    solve_problem('test2.txt', 6, None)
    solve_problem('test3.txt', None, 6)
    solve_problem('input.txt', 19099, 17099847107071)


if __name__ == '__main__':
    main()
