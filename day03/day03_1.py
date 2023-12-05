import re
from collections import deque


def has_symbol(text):
    return any(c != '.' and not c.isdigit() for c in text)


def get_part_numbers(lines):
    part_numbers = deque()
    part_number_re = re.compile(r'(\d+)')

    empty_line = '.' * (len(lines[0]) + 2)
    bordered_lines = [empty_line]
    bordered_lines.extend([f'.{line}.' for line in lines])
    bordered_lines.append(empty_line)

    for index, line in enumerate(bordered_lines):
        for match in part_number_re.finditer(line):
            start, end = match.span()
            if has_symbol(line[start-1]) \
                    or has_symbol(line[end]) \
                    or has_symbol(bordered_lines[index-1][start-1:end+1]) \
                    or has_symbol(bordered_lines[index+1][start-1:end+1]):
                part_numbers.append(int(match.group(1)))
            else:
                print(f'Rejected {match.group(1)} on line {index}')
    return part_numbers


def solve_problem(filename, expected1=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        input_data = [line.strip() for line in f.readlines()]

    result1 = sum(get_part_numbers(input_data))
    print(f"Part 1: sum of part numbers is {result1}")
    if expected1 is not None:
        assert result1 == expected1


def main():
    solve_problem('test.txt', 4361)
    solve_problem('input.txt', 539637)


if __name__ == '__main__':
    main()
