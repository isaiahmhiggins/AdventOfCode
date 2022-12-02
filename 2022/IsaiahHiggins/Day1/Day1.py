#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script evaluation Day1

import sys
import os
from pathlib import Path

currentPath = os.path.dirname(os.path.abspath(__file__))
challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")
if challengePath not in sys.path:
   sys.path.append(challengePath)

import ChallengeBase


class Day1(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)

    def getSums(self, data):
            sums = [0]
            for line in data:
                if line != "":
                    sums[-1] += int(line)
                else:
                    sums.append(0)
            return sums       

    def ExecuteP1(self, data: Path):
        with open(data, "r") as challenge_data:
            content = challenge_data.readlines()
            content = [i.strip() for i in content]
            sums = self.getSums(content)
        return max(sums)

    def ExecuteP2(self, data: Path):
        answer = 0
        contant = []
        #TODO implement evaluation
        with open(data, "r") as challenge_data:
            content = challenge_data.readlines()
            content = [i.strip() for i in content]
            sums = self.getSums(content)
            sums.sort()
            answer = sums[-1] + sums[-2] + sums[-3]
        return answer
