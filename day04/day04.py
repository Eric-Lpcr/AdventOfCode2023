
class Card:
    def __init__(self, card_id):
        self.id = card_id
        self.winning_numbers = set()
        self.owned_numbers = set()

    @property
    def owned_winning_number(self):
        return self.winning_numbers & self.owned_numbers

    @property
    def points(self):
        return int(2 ** (len(self.owned_winning_number) - 1))

    @classmethod
    def decode(cls, line):
        header, numbers = line.split(': ')
        _, card_id = header.split()
        card = Card(card_id)
        win, own = numbers.split(' | ')
        card.winning_numbers.update(map(int, win.split()))
        card.owned_numbers.update(map(int, own.split()))
        return card


def play_game(cards):
    card_counts = [1] * len(cards)
    for card_index, card in enumerate(cards):
        won_cards_count = len(card.owned_winning_number)
        new_cards_indices = (card_index + 1 + offset for offset in range(min(won_cards_count, len(cards) - card_index)))
        for new_card_index in new_cards_indices:
            card_counts[new_card_index] += card_counts[card_index]
    return card_counts


def solve_problem(filename, expected1=None, expected2=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        cards = [Card.decode(line.strip()) for line in f.readlines()]

    result1 = sum(card.points for card in cards)
    print(f"Part 1: total points is {result1}")
    if expected1 is not None:
        assert result1 == expected1

    counts = play_game(cards)
    result2 = sum(counts)
    print(f"Part 2: final number of cards is {result2}")
    if expected2 is not None:
        assert result2 == expected2


def main():
    solve_problem('test.txt', 13, 30)
    solve_problem('input.txt', 26218, 9997537)


if __name__ == '__main__':
    main()
