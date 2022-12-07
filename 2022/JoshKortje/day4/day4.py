import numpy
import copy
import itertools
import networkx as nx
import string
import re
import math
from collections import defaultdict

# Note: Should have used sets and the range() function...

def checkContainment(e1, e2):
    if e1[0] <= e2[0] and e1[1] >= e2[1]:
        return 1
    elif e1[0] >= e2[0] and e1[1] <= e2[1]:
        return 1
    else:
        return 0


def checkOverlap(e1, e2):
    if checkContainment(e1, e2) == 1:
        return 1
    elif e2[0] <= e1[0] <= e2[1]:
        return 1
    elif e2[0] <= e1[1] <= e2[1]:
        return 1
    else:
        return 0

# Start of script
file = open("input2.txt", "r")

# Split on every space
lines = list()
for line in file:
    lines.append(line.strip().split(","))

elf1 = list()
elf2 = list()
for text in lines:
    elf1.append(list(map(int, text[0].split("-"))))
    elf2.append(list(map(int, text[1].split("-"))))

contained = 0
overlap = 0
for i in range(len(elf1)):
    contained += checkContainment(elf1[i], elf2[i])
    overlap += checkOverlap(elf1[i], elf2[i])

# print results
print("Day 4")
print(contained)
print(overlap)

file.close()
