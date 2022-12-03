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

class Pack:
    def __init__(self, contentString):
        mid = int(len(contentString)/2)
        self.compartment1 = contentString[:mid]
        self.compartment2 = contentString[mid:]

    def GetDuplicate(self):
        return set(self.compartment1) & set(self.compartment2)

class Group:
    def __init__(self, pack1, pack2, pack3):
        self.pack1 = set(pack1)
        self.pack2 = set(pack2)
        self.pack3 = set(pack3)
        self.badge = list(self.DetermineBadge())[0]

    def DetermineBadge(self):
        return self.pack1 & self.pack2 & self.pack3



class Day3(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)

    def GetIssueScore(self, issue):
        answer = 0
        if issue.isupper():
            answer = ord(issue) - 38
        else:
            answer = ord(issue) - 96
        return answer

    def ExecuteP1(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
            issues = []
            for line in content:
                currentPack = Pack(line)
                duplicates = currentPack.GetDuplicate()
                issues += list(duplicates)
        for issue in issues:
            answer += self.GetIssueScore(issue)

        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
            for line in range(0, len(content), 3):
                currentGroup = Group(content[line], content[line+1], content[line+2])
                answer += self.GetIssueScore(currentGroup.badge)
        return answer
