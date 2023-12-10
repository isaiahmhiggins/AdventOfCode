import copy
from dataclasses import dataclass
from enum import Enum
import math


day_number = str(9)
sample_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_1.txt"
real_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_1.txt"
sample_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_2.txt"
real_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_2.txt"

IS_DEBUG = True

def predict_next(line: str) -> int:
    # parse line
    numbers = [int(number.strip(' \n')) for number in line.split(' ') if len(number.strip(' \n')) > 0]
    adders: list[int] = []
    current_row = copy.copy(numbers)
    if IS_DEBUG:
        print("--------")
    while not all(item == 0 for item in current_row):
        if IS_DEBUG:
            print(' '.join([str(item) for item in current_row]))
        adders.append(current_row[-1])
        next_row = []
        for i in range(len(current_row) - 1):
            next_row.append(current_row[i + 1] - current_row[i])
        current_row = next_row
    added = sum(adders)
    if IS_DEBUG:
        print("predicted: " + str(added))
    return added

def predict_before(line: str) -> int:
    # parse line
    numbers = [int(number.strip(' \n')) for number in line.split(' ') if len(number.strip(' \n')) > 0]
    adders: list[int] = []
    current_row = copy.copy(numbers)
    if IS_DEBUG:
        print("--------")
    while not all(item == 0 for item in current_row):
        if IS_DEBUG:
            print(' '.join([str(item) for item in current_row]))
        adders.append(current_row[0])
        next_row = []
        for i in range(len(current_row) - 1):
            next_row.append(current_row[i + 1] - current_row[i])
        current_row = next_row
    history_value = 0
    adders.reverse()
    for i in adders:
        history_value = i - history_value
    if IS_DEBUG:
        print("predicted: " + str(history_value))
    return history_value


def solution_part_1():
    with open(real_1, 'r') as open_file:
        lines = [line.strip() for line in open_file.readlines()]
        total = sum([predict_next(line) for line in lines])
        print("Total: " + str(total))
            
                

def solution_part_2():
    with open(real_1, 'r') as open_file:
        lines = [line.strip() for line in open_file.readlines()]
        total = sum([predict_before(line) for line in lines])
        print("Total: " + str(total))

solution_part_2()