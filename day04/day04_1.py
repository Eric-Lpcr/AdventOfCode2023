
class Card:
    def __init__(self, id):
        self.id = id
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


def solve_problem(filename, expected1=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        cards = [Card.decode(line.strip()) for line in f.readlines()]

    result1 = sum(card.points for card in cards)
    print(f"Part 1: total points is {result1}")
    if expected1 is not None:
        assert result1 == expected1


def main():
    solve_problem('test.txt', 13)
    solve_problem('input.txt', 26218)


if __name__ == '__main__':
    main()
