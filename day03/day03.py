import re
from collections import deque, defaultdict

import logging
from math import prod


def has_symbol(text):
    return any(c != '.' and not c.isdigit() for c in text)


GEAR_SYMBOL = '*'


def str_index(string, sub_string):
    """Same as str.index, but returns None instead of raising exception"""
    if sub_string in string:
        return string.index(sub_string)
    else:
        return None


def get_part_numbers(lines):
    part_numbers = deque()
    gears = defaultdict(list)
    part_number_re = re.compile(r'(\d+)')

    empty_line = '.' * (len(lines[0]) + 2)
    bordered_lines = [empty_line]
    bordered_lines.extend([f'.{line}.' for line in lines])
    bordered_lines.append(empty_line)

    for index, line in enumerate(bordered_lines):
        for match in part_number_re.finditer(line):
            start, end = match.span()
            part_number = int(match.group(1))

            before = line[start-1]
            after = line[end]
            previous_line = bordered_lines[index-1][start-1:end+1]
            next_line = bordered_lines[index+1][start-1:end+1]

            if any(map(has_symbol, (before, after, previous_line, next_line))):
                part_numbers.append(part_number)
            else:
                logging.debug(f'Rejected {part_number} on line {index}')

            if before == GEAR_SYMBOL:
                gears[(index, start-1)].append(part_number)
            if after == GEAR_SYMBOL:
                gears[(index, end)].append(part_number)
            gear_index = str_index(previous_line, GEAR_SYMBOL)
            if gear_index is not None:
                gears[(index-1, start-1+gear_index)].append(part_number)
            gear_index = str_index(next_line, GEAR_SYMBOL)
            if gear_index is not None:
                gears[(index+1, start-1+gear_index)].append(part_number)

    return part_numbers, gears


def solve_problem(filename, expected1=None, expected2=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        input_data = [line.strip() for line in f.readlines()]

    part_numbers, gears = get_part_numbers(input_data)

    result1 = sum(part_numbers)
    print(f"Part 1: sum of part numbers is {result1}")
    if expected1 is not None:
        assert result1 == expected1

    result2 = sum([prod(part_numbers) for part_numbers in gears.values() if len(part_numbers) == 2])
    print(f"Part 1: sum of gear ratios is {result2}")
    if expected2 is not None:
        assert result2 == expected2


def main():
    solve_problem('test.txt', 4361, 467835)
    solve_problem('input.txt', 539637)


if __name__ == '__main__':
    main()
