
def solve_problem(filename, expected1=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        input_data = f.readlines()

    digits = [list(map(int, filter(str.isdigit, list(line)))) for line in input_data]
    calibration_values = [digit[0] * 10 + digit[-1] for digit in digits]
    result1 = sum(calibration_values)
    print(f"Part 1: calibration values sum is {result1}")
    if expected1 is not None:
        assert result1 == expected1


def main():
    solve_problem('test.txt', 142)
    solve_problem('input.txt', 56465)


if __name__ == '__main__':
    main()
