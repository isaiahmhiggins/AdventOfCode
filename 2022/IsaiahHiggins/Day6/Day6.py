#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script evaluation Day6

import sys
import os
from pathlib import Path
from collections import Counter

currentPath = os.path.dirname(os.path.abspath(__file__))
challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")
if challengePath not in sys.path:
   sys.path.append(challengePath)

import ChallengeBase


class Day6(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)

    def isUnique(self, input):
        print(set(input))
        print(input)
        return len(set(input)) == len(input)

    def ExecuteP1(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        answer = 4
        line = content[0]
        while not self.isUnique(line[0:4]):
            answer += 1
            print(answer)
            line = line[1:]
        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        answer = 14
        line = content[0]
        while not self.isUnique(line[0:14]):
            answer += 1
            print(answer)
            line = line[1:]
        return answer
