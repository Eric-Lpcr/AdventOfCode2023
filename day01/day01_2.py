import re


def reverse(s):
    return ''.join(reversed(s))


text_figures = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
figures = {str(digit): digit for digit in range(10)}  # '1' => 1
figures.update({figure: index for index, figure in enumerate(text_figures)})  # 'one' => 1

figures_pattern = '|'.join(figures.keys())
figures_re = re.compile(rf'({figures_pattern})')
reversed_figures_re = re.compile(rf'({reverse(figures_pattern)})')


def compute_calibration_value(line):
    first_figure = re.search(figures_re, line).group(0)
    last_figure = reverse(re.search(reversed_figures_re, reverse(line)).group(0))
    return figures[first_figure] * 10 + figures[last_figure]


def solve_problem(filename, expected1=None, expected2=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        input_data = f.readlines()

    if expected1 is not None:
        digits = [list(map(int, filter(str.isdigit, list(line)))) for line in input_data]
        calibration_values = [digit[0] * 10 + digit[-1] for digit in digits]
        result1 = sum(calibration_values)
        print(f"Part 1: calibration values sum is {result1}")
        assert result1 == expected1

    if expected2 is not None:
        calibration_values = map(compute_calibration_value, input_data)
        result2 = sum(calibration_values)
        print(f"Part 2: calibration values sum is {result2}")
        assert result2 == expected2


def main():
    solve_problem('test.txt', 142)
    solve_problem('test2.txt', None, 281)
    solve_problem('input.txt', 56465, 55902)


if __name__ == '__main__':
    main()
