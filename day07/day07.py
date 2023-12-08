from collections import Counter


class Game:
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6

    CARD_ORDER_TABLE = {False: str.maketrans('TJQKA', 'abcde'),
                        True: str.maketrans('J23456789TQKA', 'abcdefghijklm')}

    JOKER = 'J'
    USE_JOKER = False

    JOKER_BONUS = {  # (hand type with cards except jokers, number of jokers): improved hand type
        (FOUR_OF_A_KIND, 1): FIVE_OF_A_KIND,
        (THREE_OF_A_KIND, 1): FOUR_OF_A_KIND, (THREE_OF_A_KIND, 2): FIVE_OF_A_KIND,
        (TWO_PAIR, 1): FULL_HOUSE,
        (ONE_PAIR, 1): THREE_OF_A_KIND, (ONE_PAIR, 2): FOUR_OF_A_KIND, (ONE_PAIR, 3): FIVE_OF_A_KIND,
        (HIGH_CARD, 1): ONE_PAIR, (HIGH_CARD, 2): THREE_OF_A_KIND, (HIGH_CARD, 3): FOUR_OF_A_KIND,
        (HIGH_CARD, 4): FIVE_OF_A_KIND, (HIGH_CARD, 5): FIVE_OF_A_KIND
    }


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    @property
    def type(self):
        card_count = Counter(self.cards)  # card: number of identical
        joker_count = card_count[Game.JOKER]
        if Game.USE_JOKER:
            del card_count[Game.JOKER]

        same_count = Counter(card_count.values())  # number of identical: number of times
        if 5 in same_count:
            type_ = Game.FIVE_OF_A_KIND
        elif 4 in same_count:
            type_ = Game.FOUR_OF_A_KIND
        elif 3 in same_count and 2 in same_count:
            type_ = Game.FULL_HOUSE
        elif 3 in same_count:
            type_ = Game.THREE_OF_A_KIND
        elif 2 in same_count and same_count[2] == 2:
            type_ = Game.TWO_PAIR
        elif 2 in same_count:  # and same_count[2] == 1:
            type_ = Game.ONE_PAIR
        else:
            type_ = Game.HIGH_CARD

        if Game.USE_JOKER:
            type_ = Game.JOKER_BONUS.get((type_, joker_count), type_)

        return type_

    def __lt__(self, other):
        self_type = self.type
        other_type = other.type
        if self_type != other_type:  # order by hand type
            return self_type < other_type
        else:  # order by card strength
            card_order_table = Game.CARD_ORDER_TABLE[Game.USE_JOKER]
            return self.cards.translate(card_order_table) < other.cards.translate(card_order_table)


def solve_problem(filename, expected1=None, expected2=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        def decode_line(line):
            cards, bid = line.split()
            return Hand(cards, int(bid))

        hands = list(map(decode_line, f.readlines()))

    Game.USE_JOKER = False
    result1 = sum((index + 1) * hand.bid for index, hand in enumerate(sorted(hands)))
    print(f"Part 1: total winnings are {result1}")
    if expected1 is not None:
        assert result1 == expected1

    Game.USE_JOKER = True
    result2 = sum((index + 1) * hand.bid for index, hand in enumerate(sorted(hands)))
    print(f"Part 2: with jokers, total winnings are {result2}")
    if expected2 is not None:
        assert result2 == expected2


def main():
    solve_problem('test.txt', 6440, 5905)
    solve_problem('input.txt', 250474325, 248909434)


if __name__ == '__main__':
    main()
