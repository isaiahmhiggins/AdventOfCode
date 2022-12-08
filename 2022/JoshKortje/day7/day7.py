import numpy
import copy
import itertools
import networkx as nx
import string
import re
import math
from collections import defaultdict
from collections import deque
#from treelib import Node, Tree
from anytree import Node, RenderTree


running_total = 0
max_size = 100000
all_directories = list()

class Size:
    def __init__(self, size):
            self.size = size


def get_size(t_node):
    global running_total
    global all_directories
    if t_node.is_leaf:
        all_directories.append(t_node.data.size)
        return t_node.data.size
    else:
        total_size = 0
        if t_node.data.size == 0:
            for child in t_node.children:
                total_size += get_size(child)
            t_node.data.size = total_size
            all_directories.append(t_node.data.size)
        if total_size <= max_size:
            running_total += total_size
        return total_size

# Start of script
file = open("input2.txt", "r")

# Split on every space
lines = list()
for line in file:
    lines.append(line.strip().split())


structure = Node("/", data=Size(0))
current_dir = structure
for cmd in lines:
    if cmd[0] == "$":
        if cmd[1] == "cd":
            if cmd[2] == "..":
                current_dir = current_dir.parent
            else:
                for c in current_dir.children:
                    if c.name == cmd[2]:
                        current_dir = c
                        break
    else:
        if cmd[0] == "dir":
            Node(cmd[1], parent=current_dir, data=Size(0))
        else:
            Node(cmd[1], parent=current_dir, data=Size(int(cmd[0])))

full_size = get_size(structure)

# Part 2
unused = 70000000 - full_size
needed = 30000000 - unused
all_directories.sort()
for dir in all_directories:
    if dir > needed:
        print("Min Directory")
        print(dir)
        break

# print results
print("Day 7")
print(running_total)
print()

file.close()
