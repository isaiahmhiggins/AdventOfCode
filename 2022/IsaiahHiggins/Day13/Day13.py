#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script evaluation Day13

import sys
import os
from pathlib import Path
from itertools import zip_longest
from functools import cmp_to_key

currentPath = os.path.dirname(os.path.abspath(__file__))
challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")
if challengePath not in sys.path:
   sys.path.append(challengePath)

import ChallengeBase


class Day13(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)
        self.id = 0

    def comparePackets(self, left, right):
        if left is None:
            return -1
        if right is None:
            return 1

        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return -1
            elif left > right:
                return 1
            else:
                return 0
        elif isinstance(left, list) and isinstance(right, list):
            for l2, r2 in zip_longest(left, right):
                if (result := self.comparePackets(l2, r2)) != 0:
                    return result
            return 0
        else:
            l2 = [left] if isinstance(left, int) else left
            r2 = [right] if isinstance(right, int) else right
            return self.comparePackets(l2, r2)

    def ExecuteP1(self, data: Path):
        answer = 0
        content = []

        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        index = 1
        for pair in range(0, len(content), 3):
            p1 = eval(content[pair])
            p2 = eval(content[pair + 1])
            if self.comparePackets(p1, p2) == -1:
                answer += index
            index += 1


        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        content = []

        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        packets = [[[2]], [[6]]]
        for pair in range(0, len(content), 3):
            p1 = eval(content[pair])
            p2 = eval(content[pair + 1])
            packets.append(p1)
            packets.append(p2)
        sorted_packets = sorted(packets, key=cmp_to_key(self.comparePackets))
        answer = (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)
        return answer
