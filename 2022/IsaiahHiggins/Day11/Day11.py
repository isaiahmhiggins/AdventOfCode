#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script evaluation Day11

import sys
import os
from pathlib import Path
import numpy as np
import math

currentPath = os.path.dirname(os.path.abspath(__file__))
challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")
if challengePath not in sys.path:
   sys.path.append(challengePath)

import ChallengeBase

class Monkey():
    def __init__(self, items, operation, test, trueIndex, falseIndex, otherMonkeys):
        self.items = items.split(': ')[1].split(', ')
        self.items = [int(i) for i in self.items]

        interest = operation.split('old ')[1].split()

        self.operation = interest[0]
        if interest[1] == 'old':
            self.operand = 'old'
        else:
            self.operand = int(interest[1])

        self.test = int(test.split('by ')[1])


        self.trueIndex = int(trueIndex.split("monkey ")[1])
        self.falseIndex = int(falseIndex.split("monkey ")[1])

        self.otherMonkeys = otherMonkeys

        self.count = 0

        self.lcm = 1

    def TakeTurn(self, part1 = True):
        for item in self.items:
            new_item = self.PerformOperation(item, part1)
            self.count += 1
            if (new_item % self.test) == 0:
                # move to true index list
                self.otherMonkeys[self.trueIndex].items.append(new_item)
            else:
                self.otherMonkeys[self.falseIndex].items.append(new_item)
        self.items = []

    def PerformOperation(self, item, part1 = True):
        new_item = int(item)
        if self.operation == "+":
            if self.operand != 'old':
                new_item = int(item) + self.operand
            else:
                new_item = int(item) + int(item)
        else: # multiply
            if self.operand != 'old':
                new_item = int(item) * self.operand
            else:
                new_item = int(item) * int(item)
        if part1:
            new_item = math.floor(new_item/3)
        else:
            new_item = new_item%self.lcm
        return new_item




class Day11(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)
        self.Monkeys = []
        self.lcm = 1

    def ExecuteP1(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        for monkey in range(0, len(content), 7):
            items = content[monkey + 1]
            operation = content[monkey + 2]
            test = content[monkey + 3]
            true_case = content[monkey + 4]
            false_case = content[monkey + 5]
            self.Monkeys.append(Monkey(items, operation, test, true_case, false_case, self.Monkeys))

        for turn in range(0, 20):
            print(f"round {turn}")
            for monkey in self.Monkeys:
                monkey.TakeTurn()
        items = [i.count for i in self.Monkeys]
        items.sort()
        answer = items[-1] * items[-2]
        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        for monkey in range(0, len(content), 7):
            items = content[monkey + 1]
            operation = content[monkey + 2]
            test = content[monkey + 3]
            true_case = content[monkey + 4]
            false_case = content[monkey + 5]
            self.Monkeys.append(Monkey(items, operation, test, true_case, false_case, self.Monkeys))

        dividers = np.array([i.test for i in self.Monkeys])
        print(dividers)
        self.lcm = int(np.prod(dividers))

        print("lcm", self.lcm)

        for turn in range(0, 100000):
            #print(turn)
            for monkey in self.Monkeys:
                monkey.lcm = self.lcm
                monkey.TakeTurn(False)
        items = [i.count for i in self.Monkeys]
        items.sort()
        answer = items[-1] * items[-2]
        return answer
