from math import prod


class Race:
    def __init__(self, time, record):
        self.time = time
        self.record = record

    def distances(self):
        return (hold_time * (self.time - hold_time) for hold_time in range(self.time))

    def number_of_ways_to_beat_record(self):
        return len(list(filter(lambda d: d > self.record, self.distances())))


def solve_problem(filename, expected1=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        times = (int(t) for t in f.readline().split()[1:])
        records = (int(r) for r in f.readline().split()[1:])
        races = list(Race(t, d) for t, d in zip(times, records))

    number_of_ways = map(Race.number_of_ways_to_beat_record, races)
    result1 = prod(number_of_ways)
    print(f"Part 1: product of number of ways to beat record is {result1}")
    if expected1 is not None:
        assert result1 == expected1


def main():
    solve_problem('test.txt', 288)
    solve_problem('input.txt', 393120)


if __name__ == '__main__':
    main()
