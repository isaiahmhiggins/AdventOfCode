import copy
from dataclasses import dataclass
import math


day_number = str(3)
sample_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_1.txt"
real_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_1.txt"
sample_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_2.txt"
real_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_2.txt"

@dataclass
class Coordinate:
    x: int
    y: int
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Coordinate):
            raise RuntimeError(f"Cannot compare {__value} to a 'Coordinate'")
        return __value.x == self.x and __value.y == self.y
    
    def is_adjacent(self, obj: 'Coordinate'):
        return abs(self.x - obj.x) <= 1 and abs(self.y - obj.y) <= 1

@dataclass
class Symbol:
    index: Coordinate
    value: str

class Number:
    indexes: list[Coordinate] = []
    value: int = 0
    max_x_coord: int = -1
    min_x_coord: int = -1

    def __init__(self, lines: list[str], coordinate: Coordinate) -> None:
        # search forward and backward to verify whole number is found
        # backward
        i = coordinate.x
        x_coords: list = []
        while i >= 0 and lines[coordinate.y][i].isdigit():
            x_coords.append(i)
            i -= 1
        
        # forward
        i = coordinate.x + 1
        while i <= len(lines[coordinate.y]) - 1 and lines[coordinate.y][i].isdigit():
            x_coords.append(i)
            i += 1
        
        self.min_x_coord = min(x_coords)
        self.max_x_coord = max(x_coords)
        unique_x_coords: list = []
        for coord in x_coords:
            if coord not in unique_x_coords:
                unique_x_coords.append(coord)
        unique_x_coords.sort()
        self.indexes = [Coordinate(x, coordinate.y) for x in unique_x_coords]
        
        # generate value
        value = 0
        # add integer times 10 to the power of position from the right
        for i in x_coords:
            digit = lines[coordinate.y][i]
            power = self.max_x_coord - i
            value += int(digit) * math.pow(10,power)
        self.value = value

def is_symbol(char: str):
    return char != '.' and not char.isdigit()


def day_3_solution_part_1():
    with open(real_1, 'r') as open_file:
        lines = [line.strip() for line in open_file.readlines()]
        symbols: list[Symbol] = []
        numbers: list[Number] = []
        good_numbers: list[Number] = []

        y = 0
        while y < len(lines):
            x = 0
            while x < len(lines[y]):
                if lines[y][x] == '.':
                    x += 1
                    continue
                if lines[y][x].isdigit():
                    coordinate = Coordinate(x, y)
                    number = Number(lines, coordinate)
                    numbers.append(number)
                    x = number.max_x_coord + 1
                    is_good_number = False
                    for i in range(number.min_x_coord - 1, number.max_x_coord + 2):
                        if i >= len(lines[y]):
                            continue
                        # Search around number
                        y_above = y - 1
                        if y_above >= 0 and i >= 0: 
                            char = lines[y_above][i]
                            if i < len(lines[y_above]) and is_symbol(char):
                                symbols.append(Symbol(Coordinate(i, y_above), char))
                                is_good_number = True
                        y_below = y + 1
                        if y_below < len(lines) and i >= 0:
                            char = lines[y_below][i]
                            if i < len(lines[y_below]) and is_symbol(char):
                                symbols.append(Symbol(Coordinate(i, y_below), char))
                                is_good_number = True
                    if number.min_x_coord - 1 >= 0 and is_symbol(lines[y][number.min_x_coord - 1]):
                        symbols.append(Symbol(Coordinate(number.min_x_coord - 1, y), lines[y][number.min_x_coord - 1]))
                        is_good_number = True
                    if number.max_x_coord + 1 < len(lines[y]) and is_symbol(lines[y][number.max_x_coord + 1]):
                        symbols.append(Symbol(Coordinate(number.min_x_coord + 1, y), lines[y][number.min_x_coord + 1]))
                        is_good_number = True
                    if is_good_number:
                        good_numbers.append(number)
                else:
                    x += 1
            y += 1

        total_value = 0
        for number in good_numbers:
            total_value += number.value
        print(f"Total: {total_value}")

def symbol_adjacent_to_numbers(numbers: list[Number], symbol: Symbol) -> list[Number]:
    adj_numbers = []
    for number in numbers:
        adj_coords = [coord for coord in number.indexes if symbol.index.is_adjacent(coord)]
        if len(adj_coords) > 0:
            adj_numbers.append(copy.copy(number))
    return adj_numbers

def day_3_solution_part_2():
    with open(real_1, 'r') as open_file:
        lines = [line.strip() for line in open_file.readlines()]
        symbols: list[Symbol] = []
        numbers: list[Number] = []

        y = 0
        while y < len(lines):
            x = 0
            while x < len(lines[y]):
                char = lines[y][x]
                if char == '.':
                    x += 1
                    continue
                coordinate = Coordinate(x, y)
                if char.isdigit():
                    number = Number(lines, coordinate)
                    numbers.append(number)
                    x = number.max_x_coord + 1
                else:
                    symbols.append(Symbol(coordinate, char))
                    x += 1
            y += 1

        total_value = 0
        
        for symbol in symbols:
            if symbol.value != "*":
                continue
            adj_numbers = symbol_adjacent_to_numbers(numbers, symbol)
            if len(adj_numbers) == 2:
                total_value += adj_numbers[0].value * adj_numbers[1].value
        print(f"Total: {total_value}")

day_3_solution_part_2()