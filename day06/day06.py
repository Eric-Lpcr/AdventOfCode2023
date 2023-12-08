from math import prod, sqrt, floor, ceil


def quadratic_roots(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2 * a)
    else:
        root1, root2 = (-b - sqrt(delta)) / (2 * a), (-b + sqrt(delta)) / (2 * a)
        if a > 0:
            return root1, root2
        else:
            return root2, root1


class Race:
    def __init__(self, time, record):
        self.time = time
        self.record = record

    def number_of_ways_to_beat_record(self):
        # distance = speed * (time - hold_time)
        # speed = hold_time
        # distance > record => distance - record > 0
        # -hold_time ** 2 + time * hold_time - record > 0
        # second degree equation... a<0 so polynom is positive between roots
        root1, root2 = quadratic_roots(-1, self.time, -self.record)

        hold_time1 = floor(root1) + 1  # first int after root1
        hold_time2 = ceil(root2) - 1  # first int before root2
        return hold_time2 - hold_time1 + 1


def solve_problem(filename, expected1=None, expected2=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        input_data = f.readlines()

    times = (int(t) for t in input_data[0].split()[1:])
    records = (int(r) for r in input_data[1].split()[1:])
    races = list(Race(t, d) for t, d in zip(times, records))

    number_of_ways = list(map(Race.number_of_ways_to_beat_record, races))
    result1 = prod(number_of_ways)
    print(f"Part 1: product of number of ways to beat record is {result1}")
    if expected1 is not None:
        assert result1 == expected1

    _, time = input_data[0].replace(' ', '').split(':')
    _, record = input_data[1].replace(' ', '').split(':')
    race = Race(int(time), int(record))

    result2 = race.number_of_ways_to_beat_record()
    print(f"Part 2: number of ways to beat record is {result2}")
    if expected2 is not None:
        assert result2 == expected2


def main():
    solve_problem('test.txt', 288, 71503)
    solve_problem('input.txt', 393120, 36872656)


if __name__ == '__main__':
    main()
