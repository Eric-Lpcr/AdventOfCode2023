from utilities.itertools_recipes import batched
from utilities.range import Range, MultiRange


class ValueMapper:
    """Adds offset to value when it's between bounds"""
    def __init__(self, in_range, offset):
        self.range = in_range
        self.offset = offset

    def apply_to_value(self, value):
        if value in self.range:
            return value + self.offset
        else:
            return None

    def apply_to_range(self, a_range):
        if a_range in self.range:
            return Range(a_range.start + self.offset, a_range.stop + self.offset)
        else:
            return None

    def cut_multirange(self, multirange):
        return multirange.cut(self.range)


class MultiMapper:
    def __init__(self):
        self.mappers = list()

    def append(self, mapper):
        self.mappers.append(mapper)

    def apply_to_value(self, value):
        """Applies mappers sequentially, returns result of first mapper which maps"""
        for mapper in self.mappers:
            result = mapper.apply_to_value(value)
            if result:
                return result
        return value

    def apply_to_multirange(self, multirange):
        all_cuts = multirange
        for mapper in self.mappers:
            all_cuts = mapper.cut_multirange(all_cuts)

        result = MultiRange()
        for cut in all_cuts.ranges:
            mapped = False
            for mapper in self.mappers:
                mapped_cut = mapper.apply_to_range(cut)
                if mapped_cut:
                    result.append(mapped_cut)
                    mapped = True
                    break
            if not mapped:
                result.append(cut)
        return result


class CompositeMapper(MultiMapper):
    """Composes mappers sequentially, returns m_n(...(m_1(value)))"""
    def __init__(self):
        super().__init__()

    def apply_to_value(self, value):
        result = value
        for mapper in self.mappers:
            result = mapper.apply_to_value(result)
        return result

    def apply_to_multirange(self, multirange):
        result = multirange
        for mapper in self.mappers:
            result = mapper.apply_to_multirange(result)
        return result


def solve_problem(filename, expected1=None, expected2=None):
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
                mapper.append(ValueMapper(Range(source, source + width), destination - source))

    locations = map(all_maps.apply_to_value, seeds)
    result1 = min(locations)
    print(f"Part 1: lowest location number is {result1}")
    if expected1 is not None:
        assert result1 == expected1

    seeds2 = MultiRange()
    for start, size in batched(seeds, 2):
        seeds2.append(Range(start, start+size))

    locations2 = all_maps.apply_to_multirange(seeds2)
    result2 = min(location.start for location in locations2.ranges)
    print(f"Part 2: lowest location number is {result2}")
    if expected2 is not None:
        assert result2 == expected2


def main():
    solve_problem('test.txt', 35, 46)
    solve_problem('input.txt', 806029445)


if __name__ == '__main__':
    main()
