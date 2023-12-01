import re


class Figures:
    mapping = {digit: int(digit) for digit in '0123456789'}  # '1' => 1
    figure_texts = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    mapping.update({figure_text: value for value, figure_text in enumerate(figure_texts)})  # 'one' => 1
    pattern = '|'.join(mapping.keys())
    first_re = re.compile(rf'({pattern})')
    last_re = re.compile(rf'(?s:.*)({pattern})')

    @classmethod
    def compute_calibration_value(cls, line):
        first_figure = re.search(cls.first_re, line).group(0)
        last_figure = re.search(cls.last_re, line).group(1)
        return cls.mapping[first_figure] * 10 + cls.mapping[last_figure]


def compute_calibration_value(line):
    digits = list(map(int, filter(str.isdigit, line)))
    return digits[0] * 10 + digits[-1]


def solve_problem(filename, expected1=None, expected2=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        input_data = f.readlines()

    if expected1 is not None:
        calibration_values = map(compute_calibration_value, input_data)
        result1 = sum(calibration_values)
        print(f"Part 1: calibration values sum is {result1}")
        assert result1 == expected1

    if expected2 is not None:
        calibration_values = map(Figures.compute_calibration_value, input_data)
        result2 = sum(calibration_values)
        print(f"Part 2: calibration values sum is {result2}")
        assert result2 == expected2


def main():
    solve_problem('test.txt', 142)
    solve_problem('test2.txt', None, 281)
    solve_problem('input.txt', 56465, 55902)


if __name__ == '__main__':
    main()
