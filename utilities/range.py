from itertools import pairwise

from utilities.itertools_recipes import flatten


# TODO
# Generalise to inclusive/exclusive edges, infinite edges
# Implement intersects, intersection, union, generator with step

class Range:
    def __init__(self, start, stop):
        self.range = range(start, stop)

    @property
    def start(self):
        return self.range.start

    @property
    def stop(self):
        return self.range.stop

    @property
    def size(self):
        return self.range.stop - self.range.start

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        return f'[{self.start}, {self.stop}['

    def __repr__(self):
        return str(self)

    def __contains__(self, item):
        if isinstance(item, Range):
            if item.is_empty() or self.is_empty():
                return False
            return self.start <= item.start and item.stop <= self.stop
        else:
            return item in self.range

    def overlaps(self, other):
        if self.is_empty() or other.is_empty():
            return False
        return self.start in other or other.start in self

    def cut(self, cutter):
        if cutter.overlaps(self):
            all_bounds = self.start, self.stop, cutter.start, cutter.stop
            all_cuts = (Range(start, stop) for start, stop in pairwise(sorted(all_bounds)))
            return tuple(cut for cut in all_cuts if cut in self)
        else:
            return self,


class MultiRange:
    def __init__(self, ranges=None):
        if ranges:
            self.ranges = list(ranges)
        else:
            self.ranges = list()  # of Range

    def append(self, a_range):
        self.ranges.append(a_range)

    @property
    def size(self):
        return sum(r.size for r in self.ranges)

    def __str__(self):
        return ' U '.join(map(str, self.ranges))

    def __repr__(self):
        return str(self)

    def __contains__(self, item):
        return any(item in r for r in self.ranges)

    def cut(self, cutter):
        return MultiRange(flatten(r.cut(cutter) for r in self.ranges))


class InclusiveRange:
    def __init__(self, begin, end):
        self.begin = min(begin, end)
        self.end = max(begin, end)

    def __contains__(self, item):
        if isinstance(item, InclusiveRange):
            return item.begin in self and item.end in self
        else:
            return self.begin <= item <= self.end

    def overlaps(self, another_range):
        return another_range.begin in self or self.begin in another_range

    def size(self):
        return self.end - self.begin + 1

    def __str__(self):
        return f'[{self.begin}, {self.end}]'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.begin == other.begin and self.end == other.end


