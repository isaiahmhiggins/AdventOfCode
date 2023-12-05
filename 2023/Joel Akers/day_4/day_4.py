import copy
from dataclasses import dataclass
import math


day_number = str(4)
sample_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_1.txt"
real_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_1.txt"
sample_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_2.txt"
real_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_2.txt"

class Card:
    winning_numbers: list[int] = []
    actual_numbers: list[int] = []

    def __init__(self, line: str):
        split_by_colon = line.split(':')
        self.number = int([part for part in split_by_colon[0].split(' ') if len(part) > 0][1].strip())
        numbers_split = split_by_colon[1].split('|')
        self.winning_numbers = [int(number) for number in numbers_split[0].strip().split(' ') if len(number) > 0]
        self.actual_numbers = [int(number) for number in numbers_split[1].strip().split(' ') if len(number) > 0]

def numbers_on_card_won(card: Card):
    return [number for number in card.actual_numbers if number in card.winning_numbers]

def day_4_solution_part_1():
    with open(real_1, 'r') as open_file:
        lines = [line.strip() for line in open_file.readlines()]
        cards = [Card(line) for line in lines]
        total_score = 0
        for card in cards:
            numbers_won = len(numbers_on_card_won(card))
            if numbers_won > 0:
                total_score += math.pow(2, numbers_won - 1)
        print(f'result: {total_score}')

def day_4_solution_part_2():
    with open(real_1, 'r') as open_file:
        card_numbers_to_count: dict[int, int] = {}
        lines = [line.strip() for line in open_file.readlines()]
        cards = [Card(line) for line in lines]
        for card in cards:
            if card.number not in card_numbers_to_count.keys():
                card_numbers_to_count[card.number] = 1
            else:
                card_numbers_to_count[card.number] += 1

            numbers_won = len(numbers_on_card_won(card))
            cards_to_copy = range(card.number + 1, card.number + numbers_won + 1)
            for i in cards_to_copy:
                if i not in card_numbers_to_count.keys():
                    card_numbers_to_count[i] = card_numbers_to_count[card.number]
                else:
                    card_numbers_to_count[i] += card_numbers_to_count[card.number]
        total = sum(card_numbers_to_count.values())
        print("total: " + str(total))




day_4_solution_part_2()