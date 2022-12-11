import numpy
import copy
import itertools
import networkx as nx
import string
import re
import math
from collections import defaultdict
from collections import deque
import cProfile
import operator
import numpy as np
from anytree import Node, RenderTree


def day11():
    master_div = 0

    class Monkey():
        def __init__(self, instr):
            self.name = int(instr[0][1][:-1])
            self.holding = deque([int(item) for item in instr[1][2:]])
            if instr[2][4] == '+':
                self.operation = operator.add
            else:
                self.operation = operator.mul
            if instr[2][5] == 'old':
                self.operand = None
            else:
                self.operand = int(instr[2][5])
            self.test_div_by = int(instr[3][-1])
            self.true_path = int(instr[4][-1])
            self.false_path = int(instr[5][-1])
            self.inspected = 0

        def throw_items(self):
            thrown = list()
            while self.holding:
                old = self.holding.popleft()
                new = eval(self.operation)
                new = int(new/3)
                self.inspected += 1
                if (new % self.test_div_by) == 0:
                    thrown.append((self.true_path, new))
                else:
                    thrown.append((self.false_path, new))
            return thrown

        def throw_items2(self):
            thrown = list()
            while self.holding:
                old = self.holding.popleft()
                if self.operand:
                    new = self.operation(old, self.operand)
                else:
                    new = self.operation(old, old)

                # Use the CRT to keep the numbers as low as possible
                new = new % master_div
                self.inspected += 1
                if (new % self.test_div_by) == 0:
                    thrown.append((self.true_path, new))
                else:
                    thrown.append((self.false_path, new))
            return thrown

    # Start of script
    file = open("input2.txt", "r")

    # Split on every space
    lines = list()
    temp = list()
    for line in file:
        if line.strip() == '':
            lines.append(temp.copy())
            temp = list()
        else:
            temp.append(line.strip().replace(',', ' ').split())

    monkeys = list()
    primes = list()
    for m in lines:
        monkeys.append(Monkey(m))
        primes.append(int(m[3][-1]))

    master_div = int(numpy.prod(primes))
    num_monkeys = len(monkeys)

    for i in range(10000):
        for m in range(num_monkeys):
            stuff = monkeys[m].throw_items2()
            for next_m, my_item in stuff:
                monkeys[next_m].holding.append(my_item)

    active = [m.inspected for m in monkeys]
    active.sort(reverse=1)

    # print results
    print("Day 11")
    print(active[0] * active[1])

    file.close()

cProfile.run("day11()")
