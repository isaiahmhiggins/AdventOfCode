#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script evaluation Day5

import sys
import os
from pathlib import Path

currentPath = os.path.dirname(os.path.abspath(__file__))
challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")
if challengePath not in sys.path:
   sys.path.append(challengePath)

import ChallengeBase

class stacks:
    def __init__(self, slice):
        """ zero is top of stack"""
        self.entry_len = 3
        self.maxRow = int(slice[-1].split()[-1])
        self.charLen = (self.maxRow * 4) -1
        self.piles = {}

        # Get Stacks from string
        for row in slice[:-1]:
            # make all rows the same length
            row = row.ljust(self.charLen, ' ')
            current_row = 1
            # look at each character spot in the string
            for entry in range(0, self.charLen, 4):
                item = row[entry:entry+self.entry_len]
                # check for no entry
                if item != '   ':
                    # make sure that key is in dict
                    if current_row not in self.piles.keys():
                        self.piles[current_row] = []
                    # add item to stack in dict
                    self.piles[current_row].append(item[1])
                current_row += 1

    def MoveItms9000(self, instruction):
        junk0, count, junk1, source, junk2, destination = instruction.split()
        count = int(count)

        # move each item from one stack to another
        for i in range(0, count):
            value = self.piles[int(source)][0]
            self.piles[int(source)].pop(0)
            self.piles[int(destination)].insert(0, value)

    def MoveItms9001(self, instruction):
        junk0, count, junk1, source, junk2, destination = instruction.split()
        count = int(count)
        intermediate = []

        # place each stack in intermediate list
        for i in range(0, count):
            value = self.piles[int(source)][0]
            self.piles[int(source)].pop(0)
            intermediate.insert(0, value)

        # since the items were prepended to the intermediate list, they have been swapped and can be added to the
        # stack in the dict
        for value in intermediate:
            self.piles[int(destination)].insert(0, value)


class Day5(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)

    def ExecuteP1(self, data: Path):
        answer = ""
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip('\n') for i in challenge_data.readlines()]
            # extract the stacks from the instructions
            stacks_whole = content[:content.index('')]
            movements = content[content.index('') + 1:]
            cargo = stacks(stacks_whole)

            for instruction in movements:
                cargo.MoveItms9000(instruction)

        # Get the top item in each column
        keys = list(cargo.piles.keys())
        keys.sort()
        for key in keys:
            answer += cargo.piles[key][0]

        return answer

    def ExecuteP2(self, data: Path):
        answer = ""
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip('\n') for i in challenge_data.readlines()]
            stacks_whole = content[:content.index('')]
            movements = content[content.index('') + 1:]
            cargo = stacks(stacks_whole)

            for instruction in movements:
                cargo.MoveItms9001(instruction)

        keys = list(cargo.piles.keys())
        keys.sort()
        for key in keys:
            answer += cargo.piles[key][0]

        return answer
