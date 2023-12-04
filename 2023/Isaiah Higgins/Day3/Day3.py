#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script evaluation Day3

import sys
import os
from pathlib import Path

currentPath = os.path.dirname(os.path.abspath(__file__))
challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")
if challengePath not in sys.path:
   sys.path.append(challengePath)

import ChallengeBase

class Schematic():
    def __init__(self, content):
        self.content = []
        for line in content:
            line_chars = []
            for char in line:
                line_chars.append(char)
            self.content.append(line_chars)

    def GetAdjscentNumbers(self, row, col):
        top_left = self.GetFullNumber(row - 1, col - 1)
        top_middle = self.GetFullNumber(row - 1, col)
        top_right = self.GetFullNumber(row - 1, col + 1)
        left = self.GetFullNumber(row, col - 1)
        right = self.GetFullNumber(row, col + 1)
        bottom_left = self.GetFullNumber(row + 1, col - 1)
        bottom_middle = self.GetFullNumber(row + 1, col)
        bottom_right = self.GetFullNumber(row + 1, col + 1)

        top = {top_left, top_middle, top_right}
        bottom = {bottom_left, bottom_middle, bottom_right}

        # filter out Nones
        top = [i for i in top if i != None]
        bottom = [i for i in bottom if i != None]

        all_nums = []

        if top != None:
            all_nums.extend(top)
        if bottom != None:
            all_nums.extend(bottom)
        if left != None:
            all_nums.extend([left])
        if right  != None:
            all_nums.extend([right])

        return all_nums

        # todo filter numbers

    def GetFullNumber(self, row, col):
        number = ""
        # only fill string if number exists
        if self.content[row][col].isnumeric():
            #get start of number
            row_start = row
            col_start = col

            while(self.content[row_start][col_start].isnumeric() and col_start >= 0):
                col_start -= 1

            # increment back to start
            col_start += 1

            #fill full number
            self.content[row_start][col_start]
            while(col_start < len(self.content[0]) and self.content[row_start][col_start].isnumeric()):
                number += self.content[row_start][col_start]
                col_start += 1
            return int(number)



class Day3(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)

    def ExecuteP1(self, data: Path):
        answer = 0
        content = []

        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        schematic = Schematic(content)
        for row in range(len(schematic.content)):
            for col in range(len(schematic.content[0])):
                if schematic.content[row][col] != '.' and not schematic.content[row][col].isnumeric():
                    id = schematic.GetAdjscentNumbers(row, col)
                    for num in id:
                        answer += num



        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        schematic = Schematic(content)
        for row in range(len(schematic.content)):
            for col in range(len(schematic.content[0])):
                if schematic.content[row][col] == '*':
                    id = schematic.GetAdjscentNumbers(row, col)
                    if len(id) == 2:
                        ratio = id[0] * id[1]
                        answer += ratio

        return answer
