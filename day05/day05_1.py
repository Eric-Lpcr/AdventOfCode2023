
class RangeMapper:
    """Adds offset to value when it's between bounds"""
    def __init__(self, lower_bound, upper_bound, offset):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.offset = offset

    def __call__(self, value):
        if self.lower_bound <= value <= self.upper_bound:
            return value + self.offset
        else:
            return value


class MultiMapper:
    """Applies mappers sequentially, returns on first mapper which changes the value"""
    def __init__(self):
        self.mappers = list()

    def append(self, mapper):
        self.mappers.append(mapper)

    def __call__(self, value):
        for mapper in self.mappers:
            result = mapper(value)
            if result != value:
                return result
        return value


class CompositeMapper(MultiMapper):
    """Composes mappers sequentially, returns m_n(...(m_1(value)))"""
    def __init__(self):
        super().__init__()

    def __call__(self, value):
        result = value
        for mapper in self.mappers:
            result = mapper(result)
        return result


def solve_problem(filename, expected1=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        blocks = f.read().split('\n\n')
        _, seeds_text = blocks[0].split(': ')
        seeds = list(map(int, seeds_text.split()))
        all_maps = CompositeMapper()
        for map_block in blocks[1:]:
            mapper = MultiMapper()
            all_maps.append(mapper)
            for map_line in map_block.split('\n'):
                if map_line.endswith('map:'):
                    continue
                destination, source, width = list(map(int, map_line.split()))
                mapper.append(RangeMapper(source, source + width, destination - source))

    locations = map(all_maps, seeds)
    result1 = min(locations)
    print(f"Part 1: lowest location number is {result1}")
    if expected1 is not None:
        assert result1 == expected1


def main():
    solve_problem('test.txt', 35)
    solve_problem('input.txt', 806029445)


if __name__ == '__main__':
    main()
