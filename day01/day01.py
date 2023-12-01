import re


class Figures:
    texts = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    mapping = {str(digit): digit for digit in range(10)}  # '1' => 1
    mapping.update({figure: index for index, figure in enumerate(texts)})  # 'one' => 1
    pattern = '|'.join(mapping.keys())
    first_re = re.compile(rf'({pattern})')
    last_re = re.compile(rf'(?s:.*)({pattern})')

    @classmethod
    def value_of(cls, text):
        return cls.mapping[text]


def compute_calibration_value(line):
    first_figure = re.search(Figures.first_re, line).group(0)
    last_figure = re.search(Figures.last_re, line).group(1)
    return Figures.value_of(first_figure) * 10 + Figures.value_of(last_figure)


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
