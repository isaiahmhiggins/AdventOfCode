#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script evaluation Day4

import sys
import os
from pathlib import Path

currentPath = os.path.dirname(os.path.abspath(__file__))
challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")
if challengePath not in sys.path:
   sys.path.append(challengePath)

import ChallengeBase

class elf:
    def __init__(self, entry):
        self.start, self.end = entry.split('-')
        self.start = int(self.start)
        self.end = int(self.end)


class Day4(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)

    def ExecuteP1(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
            for line in content:
                elf1_entry, elf2_entry = line.split(',')
                elf1 = elf(elf1_entry)
                elf2 = elf(elf2_entry)

                if elf1.start <= elf2.start and elf1.end >= elf2.end:
                    answer+=1
                elif elf2.start <= elf1.start and elf2.end >= elf1.end:
                    answer += 1
        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
            for line in content:
                elf1_entry, elf2_entry = line.split(',')
                elf1 = elf(elf1_entry)
                elf2 = elf(elf2_entry)

                if elf1.start <= elf2.start <= elf1.end:
                    answer += 1
                elif elf2.start <= elf1.start <= elf2.end:
                    answer += 1

        return answer
