import numpy
import copy
import itertools
import networkx as nx
import string
import re
import math
from collections import defaultdict


# Start of script
file = open("input2.txt", "r")

# Split on every space
lines = list()
elves = list()
elf = 0
for line in file:
    if line.strip():
        elf += int(line.strip())
    else:
        elves.append(elf)
        elf = 0

# part 2
elves.sort(reverse=1)


# print results
print("Day 1")
print(elves)
print(max(elves))
print(elves[0] + elves[1] + elves[2])

file.close()
