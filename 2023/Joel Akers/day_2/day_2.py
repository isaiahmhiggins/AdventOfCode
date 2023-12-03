from enum import Enum


sample_1 = "./day_2/sample_1.txt"
real_1 = "./day_2/real_1.txt"

sample_2 = "./day_2/sample_2.txt"
real_2 = "./day_2/real_2.txt"

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

def str_to_color(string: str):
    if string == Color.RED.value:
        return Color.RED
    if string == Color.GREEN.value:
        return Color.GREEN
    return Color.BLUE

class Round:

    def __init__(self, string: str) -> None:
        collections = string.strip().split(',')
        self._color_to_count = {}
        for collection_str in collections:
            collection_split = collection_str.strip().split(' ')

            self._color_to_count[str_to_color(collection_split[1].strip())] = int(collection_split[0])
    @property
    def color_to_count(self) -> dict:
        return self._color_to_count


class Game:

    def __init__(self, line: str) -> None:
        colon_split = line.split(':')
        self._number = int(colon_split[0].split(' ')[1])
        round_lines = colon_split[1].strip().split(';')
        self._rounds = [Round(round) for round in round_lines]

    @property
    def number(self) -> int:
        return self._number
    
    @property
    def rounds(self) -> list[Round]:
        return self._rounds

def day_2_solution_part_1():
    color_to_max_count = {
        Color.RED: 12,
        Color.BLUE: 14,
        Color.GREEN: 13
    }
    with open(real_1, 'r') as open_file:
        games: list(Game) = []
        for line in open_file.readlines():
            next_game = Game(line)
            games.append(next_game)

        possible_game_count = 0
        for game in games:
            possible = True
            for round in game.rounds:
                if not possible:
                    continue
                if Color.RED in round.color_to_count.keys():
                    round_color_count = round.color_to_count[Color.RED]
                    color_max_count = color_to_max_count[Color.RED]
                    if round_color_count > color_max_count:
                        possible = False
                
                if Color.BLUE in round.color_to_count.keys():
                    round_color_count = round.color_to_count[Color.BLUE]
                    color_max_count = color_to_max_count[Color.BLUE]
                    if round_color_count > color_max_count:
                        possible = False
                
                if Color.GREEN in round.color_to_count.keys():
                    round_color_count = round.color_to_count[Color.GREEN]
                    color_max_count = color_to_max_count[Color.GREEN]
                    if round_color_count > color_max_count:
                        possible = False
            if possible:
                possible_game_count += game.number
        print(f"Total Possible Games: {possible_game_count}")

def day_2_solution_part_2():
    with open(real_1, 'r') as open_file:
        games: list(Game) = []
        for line in open_file.readlines():
            next_game = Game(line)
            games.append(next_game)

        power_total = 0
        for game in games:
            max_red = 0
            max_blue = 0
            max_green = 0

            for round in game.rounds:
                if Color.RED in round.color_to_count.keys():
                    round_color_count = round.color_to_count[Color.RED]
                    max_red = max([max_red, round_color_count])
                if Color.BLUE in round.color_to_count.keys():
                    round_color_count = round.color_to_count[Color.BLUE]
                    max_blue = max([max_blue, round_color_count])
                
                if Color.GREEN in round.color_to_count.keys():
                    round_color_count = round.color_to_count[Color.GREEN]
                    max_green = max([max_green, round_color_count])

            game_power = max_red * max_blue * max_green
            print(f"Game Power = {max_red} * {max_blue} * {max_green} = {game_power}")
            power_total += game_power
        print(f"Total Games Power: {power_total}")

day_2_solution_part_2()

        