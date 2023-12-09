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
    key: int
    right: str
    left: str
    is_start: bool
    is_end: bool
    def __init__(self, line: str, key: int) -> None:
        equal_split = line.split('=')
        left_right_split = equal_split[1].strip(' ()\n').split(',')
        self.left = left_right_split[0].strip()
        self.right = left_right_split[1].strip()
        string_key =  equal_split[0].strip()
        self.is_start = string_key[2] == 'A'
        self.is_end = string_key[2] == 'Z'
        self.key = key


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
        node_list = []
        for i in range(2, len(lines)):
            if len(lines[i]) > 0:
                node_list.append(Node(lines[i], i))
        
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
        node_list = []
        for i in range(2, len(lines)):
            if len(lines[i]) > 0:
                node_list.append(Node(lines[i], i))
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
            for step in current_steps:
                if current_turn == 'R':
                    next_steps.append(node_map.get_right(step))
                elif current_turn == 'L':
                    next_steps.append(node_map.get_left(step))
                else:
                    print('Somethings going wrong with the sequence.')
            current_steps = next_steps
            sequence_index += 1
            if steps_count % 10000000 == 0:
                print('current steps: ' + str(steps_count))
        print("Total Steps: " + str(steps_count))


solution_part_2()