import numpy
import copy
import itertools
import networkx as nx
import string
import re
import math
from collections import defaultdict
from collections import deque


# Start of script
file = open("input2.txt", "r")

size = 14

# Split on every space
text = file.read()
header = 0
for i in range(size,len(text)):
    buckets = set(list(text[i-size:i]))
    if len(buckets) == size:
        header = i
        break


# print results
print("Day 6")
print(header)

file.close()
