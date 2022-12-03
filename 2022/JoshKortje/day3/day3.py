import numpy
import copy
import itertools
import networkx as nx
import string
import re
import math
from collections import defaultdict

def get_score(input):
    total = 0
    for char in [list(left) for left in input]:
        curr = ord(char[0])
        if 65 <= curr <= 90:
            curr = curr - 38
        elif 97 <= curr <= 122:
            curr = curr - 96
        total += curr
    return total

# Start of script
file = open("input2.txt", "r")

# Split on every space
lines = list()
for line in file:
    lines.append(line.split())

comp1 = list()
comp2 = list()
for text in lines:
    comp1.append(text[0][0:int(len(text[0])/2)])
    comp2.append(text[0][int(len(text[0])/2):])

common = list()
for i in range(len(comp1)):
    common.append(set(comp1[i]) & set(comp2[i]))

score = get_score(common)

# Part 2
badge = list()
for i in range(0, len(lines), 3):
    badge.append(list(set(lines[i+0][0]) & set(lines[i+1][0]) & set(lines[i+2][0])))

print(badge)
part2 = get_score(badge)

# print results
print("Day 3")
print(score)
print(part2)

file.close()
