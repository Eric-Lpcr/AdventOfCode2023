from utilities.itertools_recipes import pairwise


def extrapolate(history):
    differences = list(history)
    extrapolated = history[-1]
    while any(differences):
        differences = [y-x for x, y in pairwise(differences)]
        extrapolated += differences[-1]
    return extrapolated


def solve_problem(filename, expected1=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        histories = [list(map(int, line.strip().split())) for line in f.readlines()]

    result1 = sum(map(extrapolate, histories))
    print(f"Part 1: sum of extrapolated values is {result1}")
    if expected1 is not None:
        assert result1 == expected1


def main():
    solve_problem('test.txt', 114)
    solve_problem('input.txt', 2075724761)


if __name__ == '__main__':
    main()
