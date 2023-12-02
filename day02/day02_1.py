

class GameSet:
    def __init__(self, red_cubes=0, green_cubes=0, blue_cubes=0):
        self.red_cubes = red_cubes
        self.green_cubes = green_cubes
        self.blue_cubes = blue_cubes

    def is_possible(self, bag):
        return (self.red_cubes <= bag.red_cubes
                and self.green_cubes <= bag.green_cubes
                and self.blue_cubes <= bag.blue_cubes)

    @staticmethod
    def decode(text: str):  # '1 red, 2 green, 6 blue'
        game_set = GameSet()
        for cubes in text.split(', '):
            count, color = cubes.split()
            count = int(count)
            if 'red' in color:
                game_set.red_cubes = count
            if 'green' in cubes:
                game_set.green_cubes = count
            if 'blue' in cubes:
                game_set.blue_cubes = count
        return game_set


class Game:
    def __init__(self, game_id):
        self.game_id = game_id
        self.game_sets = list()

    def is_possible(self, bag):
        return all(map(lambda game_set: game_set.is_possible(bag), self.game_sets))

    @staticmethod
    def decode(text: str):  # 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        header, sets_text = text.split(': ')
        _, game_id = header.split(' ')
        game = Game(int(game_id))
        for set_text in sets_text.split('; '):
            game.game_sets.append(GameSet.decode(set_text))
        return game


def solve_problem(filename, expected1=None):
    print(f'--------- {filename}')

    with open(filename) as f:
        games = map(Game.decode, f.readlines())

    bag = GameSet(red_cubes=12, green_cubes=13, blue_cubes=14)
    result1 = sum([game.game_id for game in games if game.is_possible(bag)])
    print(f"Part 1: sum of possible games ids is {result1}")
    if expected1 is not None:
        assert result1 == expected1


def main():
    solve_problem('test.txt', 8)
    solve_problem('input.txt', 2101)


if __name__ == '__main__':
    main()
