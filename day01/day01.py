import re


class CalibrationDecoder:
    figure_mapping = {digit: int(digit) for digit in '0123456789'}  # '1' => 1
    figure_texts = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    figure_mapping.update({figure_text: value for value, figure_text in enumerate(figure_texts)})  # 'one' => 1
    figure_regex = '|'.join(figure_mapping.keys())
    first_pattern = re.compile(rf'({figure_regex})')
    last_pattern = re.compile(rf'(?s:.*)({figure_regex})')

    @staticmethod
    def decode_digits(line):
        digits = list(map(int, filter(str.isdigit, line)))
        return digits[0] * 10 + digits[-1]

    @classmethod
    def decode_figures(cls, line):
        first_figure = cls.first_pattern.search(line).group(1)
        last_figure = cls.last_pattern.search(line).group(1)
        return cls.figure_mapping[first_figure] * 10 + cls.figure_mapping[last_figure]


def solve_problem(filename, expected1=None, expected2=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        input_data = [line.strip() for line in f.readlines()]

    if expected1 is not None:
        calibration_values = map(CalibrationDecoder.decode_digits, input_data)
        result1 = sum(calibration_values)
        print(f"Part 1: calibration values sum is {result1}")
        assert result1 == expected1

    if expected2 is not None:
        calibration_values = map(CalibrationDecoder.decode_figures, input_data)
        result2 = sum(calibration_values)
        print(f"Part 2: calibration values sum is {result2}")
        assert result2 == expected2


def main():
    solve_problem('test.txt', 142)
    solve_problem('test2.txt', None, 281)
    solve_problem('input.txt', 56465, 55902)


if __name__ == '__main__':
    main()
