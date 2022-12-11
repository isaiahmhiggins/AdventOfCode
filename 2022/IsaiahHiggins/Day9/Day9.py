#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script evaluation Day9

import sys
import os
from pathlib import Path

currentPath = os.path.dirname(os.path.abspath(__file__))
challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")
if challengePath not in sys.path:
   sys.path.append(challengePath)

import ChallengeBase


class Day9(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)
        # start off at index x = 0, y = 0
        self.head_pos = (0, 0)
        self.knots = []
        for i in range(0, 9):
            self.knots.append((0, 0))
        self.tail_pos = (0, 0)
        self.covered_tail = {(0, 0)}

    def Move_Head(self, direction, length):
        head_x, head_y = self.head_pos
        for step in range(0, int(length)):
            if direction == "U":
                head_y += 1
            elif direction == "D":
                head_y -= 1
            elif direction == "L":
                head_x -= 1
            elif direction == "R":
                head_x += 1
            self.head_pos = (head_x, head_y)
            self.knots[0] = self.Move_Tail(head_x, head_y, self.knots[0][0], self.knots[0][1])
            for knot in range(1, len(self.knots)):
                k1_x, k1_y = self.knots[knot - 1]
                k2_x, k2_y = self.knots[knot]
                self.knots[knot] = self.Move_Tail(k1_x, k1_y, k2_x, k2_y)

            self.covered_tail.add(self.knots[-1])

    def Move_Rope(self, direction, length):
        head_x, head_y = self.head_pos
        for step in range(0, int(length)):
            if direction == "U":
                head_y += 1
            elif direction == "D":
                head_y -= 1
            elif direction == "L":
                head_x -= 1
            elif direction == "R":
                head_x += 1
            self.head_pos = (head_x, head_y)
            for position in range(len(self.knots)):
                self.tail_pos = self.Move_Tail(head_x, head_y, self.tail_pos)
            self.covered_tail.add(self.tail_pos)

    def Move_Tail(self, head_x, head_y, tail_x, tail_y):
        # head 2 above direct
        if head_x == tail_x and head_y > tail_y and abs(head_y - tail_y) >= 2:
            tail_y += 1
        # head 2 below direct
        elif head_x == tail_x and head_y < tail_y and abs(head_y - tail_y) >= 2:
            tail_y -= 1
        # head 2 right direct
        elif head_y == tail_y and head_x > tail_x and abs(head_x - tail_x) >= 2:
            tail_x += 1
        # head 2 left direct
        elif head_y == tail_y and head_x < tail_x and abs(head_x - tail_x) >= 2:
            tail_x -= 1
        # head 2 above diagnoal
        if head_x != tail_x and head_y > tail_y and abs(head_y - tail_y) >= 2:
            tail_y += 1
            if head_x > tail_x:
                tail_x += 1
            else:
                tail_x -= 1
        # head 2 below diagonal
        elif head_x != tail_x and head_y < tail_y and abs(head_y - tail_y) >= 2:
            tail_y -= 1
            if head_x > tail_x:
                tail_x += 1
            else:
                tail_x -= 1
        # head right diagonal
        elif head_y != tail_y and head_x > tail_x and abs(head_x - tail_x) >= 2:
            tail_x += 1
            if head_y > tail_y:
                tail_y += 1
            else:
                tail_y -= 1
        # head left diagonal
        elif head_y != tail_y and head_x < tail_x and abs(head_x - tail_x) >= 2:
            tail_x -= 1
            if head_y > tail_y:
                tail_y += 1
            else:
                tail_y -= 1

        return (tail_x, tail_y)


    def ExecuteP1(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        for line in content:
            direction, distance = line.split()
            self.Move_Head(direction, distance)
        answer = len(self.covered_tail)
        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        content = []
        #TODO implement evaluation
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        for line in content:
            direction, distance = line.split()
            self.Move_Head(direction, distance)
        answer = len(self.covered_tail)
        return answer
