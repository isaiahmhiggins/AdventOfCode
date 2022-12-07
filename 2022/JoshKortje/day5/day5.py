import numpy
import copy
import itertools
import networkx as nx
import string
import re
import math
from collections import defaultdict
from collections import deque

# Note: Should have used sets and the range() function...



# Start of script
file = open("input2.txt", "r")

# Split on every space
lines = list()
init_done = 0
for line in file:
    if line[0] == '\n':
        init_done = 1
        lines.append(list(line))
        continue
    if init_done == 0:
        lines.append(list(line))
    else:
        lines.append(line.strip().split())

stacks = [deque() for i in range(9)]
init_done = 0
instructions = list()
for line in lines:
    if line[0] == '\n':
        init_done = 1
        continue
    if init_done == 0:
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                stacks[(i-1)//4].appendleft(line[i])
    else:
        instructions.append((int(line[1]), int(line[3]), int(line[5])))

# Part 1
#for inst in instructions:
#    for i in range(0, inst[0]):
#        temp = stacks[inst[1]-1].pop()
#        stacks[inst[2]-1].append(temp)

# part 2
for inst in instructions:
    temp = list()
    for i in range(0, inst[0]):
        temp.append(stacks[inst[1]-1].pop())
    for i in range(inst[0], 0, -1):
        stacks[inst[2]-1].append(temp[i - 1])

message = ''.join([s.pop() for s in stacks])

# print results
print("Day 5")
print(message)

file.close()
