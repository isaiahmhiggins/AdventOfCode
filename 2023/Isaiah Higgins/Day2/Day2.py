#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script evaluation Day2

import sys
import os
from pathlib import Path

currentPath = os.path.dirname(os.path.abspath(__file__))
challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")
if challengePath not in sys.path:
   sys.path.append(challengePath)

import ChallengeBase


class Day2(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)

    def ExecuteP1(self, data: Path):
        answer = 0
        content = []
        #TODO implement evaluation
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
            print("part1 unevaluated")
        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        content = []
        #TODO implement evaluation
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
            print("part2 unevaluated")
        return answer
