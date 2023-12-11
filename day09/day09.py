from utilities.itertools_recipes import pairwise


def extrapolate(history):
    differences = list(history)
    extrapolated = history[-1]
    while any(differences):
        differences = [y-x for x, y in pairwise(differences)]
        extrapolated += differences[-1]
    return extrapolated


def extrapolate_back(history):
    differences = list(history)
    extrapolated = history[0]
    sign = -1
    while any(differences):
        differences = [y-x for x, y in pairwise(differences)]
        extrapolated += sign * differences[0]
        sign = -sign
    return extrapolated


def solve_problem(filename, expected1=None, expected2=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        histories = [list(map(int, line.strip().split())) for line in f.readlines()]

    result1 = sum(map(extrapolate, histories))
    print(f"Part 1: sum of extrapolated values is {result1}")
    if expected1 is not None:
        assert result1 == expected1

    # result2 = sum(map(extrapolate_back, histories))
    result2 = sum(map(extrapolate, [list(reversed(history)) for history in histories]))
    print(f"Part 2: sum of backward extrapolated values is {result2}")
    if expected2 is not None:
        assert result2 == expected2


def main():
    solve_problem('test.txt', 114, 2)
    solve_problem('input.txt', 2075724761, 1072)


if __name__ == '__main__':
    main()
