import copy
from dataclasses import dataclass
from enum import Enum
import math


day_number = str(8)
sample_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_1.txt"
real_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_1.txt"
sample_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_2.txt"
real_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_2.txt"

IS_DEBUG = True

class Node:
    key: str
    right: str
    left: str
    is_start: bool
    is_end: bool
    def __init__(self, line: str) -> None:
        equal_split = line.split('=')
        left_right_split = equal_split[1].strip(' ()\n').split(',')
        self.left = left_right_split[0].strip()
        self.right = left_right_split[1].strip()
        self.key = equal_split[0].strip()
        self.is_start = self.key[2] == 'A'
        self.is_end = self.key[2] == 'Z'


class NodeMap:
    nodes: dict[str, dict[str, dict[str, Node]]] = {}

    def __init__(self, node_list: list[Node]) -> None:
        for node in node_list:
            if node.key[0] not in self.nodes.keys():
                self.nodes[node.key[0]] = {node.key[1]: {node.key[2]: node}}
            elif node.key[1] not in self.nodes[node.key[0]].keys():
                self.nodes[node.key[0]][node.key[1]] = {node.key[2]: node}
            else:
                self.nodes[node.key[0]][node.key[1]][node.key[2]] = node
    
    def get_right(self, key: str) -> str:
        return self.nodes[key[0]][key[1]][key[2]].right
    def get_left(self, key: str) -> str:
        return self.nodes[key[0]][key[1]][key[2]].left


def solution_part_1():
    with open(real_1, 'r') as open_file:
        lines = [line.strip() for line in open_file.readlines()]
        right_left_sequence = lines[0].strip()
        node_list = [Node(line) for line in lines[1:] if len(line) > 0]
        
        node_dict = {node.key[0]: node for node in node_list}

        expected_start = 'AAA'
        expected_end = 'ZZZ'
        current_step = copy.copy(expected_start)
        sequence_index = 0
        steps_count = 0
        while current_step != expected_end:
            steps_count += 1
            if sequence_index == len(right_left_sequence):
                sequence_index = 0
            current_node = node_dict[current_step]
            current_turn = right_left_sequence[sequence_index]
            if current_turn == 'R':
                current_step = current_node.right
            else:
                current_step = current_node.left
            
            sequence_index += 1
        print("Total Steps: " + str(steps_count))
            
                

def solution_part_2():
    with open(real_1, 'r') as open_file:
        lines = [line.strip() for line in open_file.readlines()]
        
        right_left_sequence = lines[0].strip()
        node_list = [Node(line) for line in lines[1:] if len(line) > 0]
        node_map = NodeMap(node_list)
        starting_keys = [node.key for node in node_list if node.key[2] == 'A']

        current_steps = copy.copy(starting_keys)
        sequence_index = 0
        steps_count = 0
        while not all([step[2] == 'Z' for step in current_steps]):
            steps_count += 1
            if sequence_index == len(right_left_sequence):
                sequence_index = 0
            next_steps = []
            current_turn = right_left_sequence[sequence_index]
            reached_a_possible_end = False
            for step in current_steps:
                if current_turn == 'R':
                    right_key = node_map.get_right(step)
                    if right_key[2] == 'Z':
                        reached_a_possible_end = True
                    next_steps.append(right_key)
                elif current_turn == 'L':
                    left_key = node_map.get_left(step)
                    if left_key[2] == 'Z':
                        reached_a_possible_end = True
                    next_steps.append(left_key)
                else:
                    print('Somethings going wrong with the sequence.')
            if reached_a_possible_end:
                print("-------------")
                print("step " + str(steps_count))
                for i in range(len(next_steps)):
                    print(f"S: {starting_keys[i]}, Z: {next_steps[i]}")
                print("--------------")
            current_steps = next_steps
            sequence_index += 1
            if steps_count % 10000000 == 0:
                print('current steps: ' + str(steps_count))
        print("Total Steps: " + str(steps_count))


#solution_part_2()

import math

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def find_lcd(numbers):
    if not numbers:
        return None

    # Initialize the result with the first number in the list
    result = numbers[0]

    # Iterate through the list of numbers and find the LCD
    for num in numbers[1:]:
        # Use the GCD to find the LCD
        result = (result * num) // find_gcd(result, num)

    return result

paths = [19631, 13771, 21389, 17287, 23147, 20803]
result = find_lcd(paths)
print('result: ' + str(result))