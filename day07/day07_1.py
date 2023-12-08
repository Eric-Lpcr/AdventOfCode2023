from enum import IntEnum
from collections import Counter


class HandType(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    @property
    def type(self):
        card_count = Counter(self.cards)  # card: number of identical
        same_count = Counter(card_count.values())  # number of identical: number of times
        if 5 in same_count:
            return HandType.FIVE_OF_A_KIND
        elif 4 in same_count:
            return HandType.FOUR_OF_A_KIND
        elif 3 in same_count and 2 in same_count:
            return HandType.FULL_HOUSE
        elif 3 in same_count:
            return HandType.THREE_OF_A_KIND
        elif 2 in same_count and same_count[2] == 2:
            return HandType.TWO_PAIR
        elif 2 in same_count:
            return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD

    CARD_ORDER_TABLE = str.maketrans('TJQKA', 'abcde')  # digits are already ordered and are lower than letters

    def __lt__(self, other):
        self_type = self.type
        other_type = other.type
        if self_type == other_type:
            return self.cards.translate(self.CARD_ORDER_TABLE) < other.cards.translate(self.CARD_ORDER_TABLE)
        else:
            return self_type < other_type


def solve_problem(filename, expected1=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        def decode_line(line):
            cards, bid = line.split()
            return Hand(cards, int(bid))

        hands = list(map(decode_line, f.readlines()))

    result1 = sum((index + 1) * hand.bid for index, hand in enumerate(sorted(hands)))
    print(f"Part 1: total winnings are {result1}")
    if expected1 is not None:
        assert result1 == expected1


def main():
    solve_problem('test.txt', 6440)
    solve_problem('input.txt', 250474325)


if __name__ == '__main__':
    main()
