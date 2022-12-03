import numpy
import copy
import itertools
import networkx as nx
import string
import re
import math
from collections import defaultdict

points = defaultdict()
# part 1
#points["A X"] = 4
#points["B X"] = 1
#points["C X"] = 7
#points["A Y"] = 8
#points["B Y"] = 5
#points["C Y"] = 2
#points["A Z"] = 3
#points["B Z"] = 9
#points["C Z"] = 6

# part 2
points["A X"] = 3
points["B X"] = 1
points["C X"] = 2
points["A Y"] = 4
points["B Y"] = 5
points["C Y"] = 6
points["A Z"] = 8
points["B Z"] = 9
points["C Z"] = 7

# Start of script
file = open("input2.txt", "r")

# Split on every space
lines = list()
score = 0
for line in file:
    print(line)
    print(points[line.strip()])
    score += points[line.strip()]


# print results
print("Day 2")
print(score)

file.close()
