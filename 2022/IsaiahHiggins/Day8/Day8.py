#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script evaluation Day8

import sys
import os
from pathlib import Path
import numpy as np

currentPath = os.path.dirname(os.path.abspath(__file__))
challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")
if challengePath not in sys.path:
   sys.path.append(challengePath)

import ChallengeBase


class Day8(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)

    def getEdgeVisible(self, trees):
        return (len(trees) *2) + (len(trees[0]) * 2) - 4

    def isVisibleT(self, trees, row, column):

        value = trees[row][column]

        trees = np.array(trees)
        above = trees[:row, column]
        below = trees[row+1:, column]
        left = trees[row, :column]
        right = trees[row, column+1:]

        topHidden = len([*filter(lambda x: x >= value, above)]) > 0
        bottomHidden = len([*filter(lambda x: x >= value, below)]) > 0
        leftHidden = len([*filter(lambda x: x >= value, left)]) > 0
        rightHidden = len([*filter(lambda x: x >= value, right)]) > 0


        return (not topHidden) or (not bottomHidden) or (not leftHidden) or (not rightHidden)

    def getViewDistance(self, trees, row, column):
        trees = np.array(trees)
        value = trees[row, column]
        above = np.array(trees[:row, column])
        below = np.array(trees[row+1:, column])
        left = np.array(trees[row, :column])
        right = np.array(trees[row, column+1:])


        rightScore = 0
        leftScore = 0
        upScore = 0
        downScore = 0

        for height in np.flipud(above):
            upScore += 1
            if height >= value:
                break

        for height in below:
            downScore += 1
            if height >= value:
                break

        for height in right:
            rightScore += 1
            if height >= value:
                break


        for height in np.flipud(left):
            leftScore += 1
            if height >= value:
                break

        return rightScore * leftScore * upScore * downScore


    def ExecuteP1(self, data: Path):
        answer = 0
        content = []
        #TODO implement evaluation
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
            trees = []
            for line in content:
                trees.append(list(line))
            for col in range(1, len(trees)-1):
                for row in range(1, len(trees[0])-1):
                    if self.isVisibleT(trees, row, col):
                        answer += 1

            answer += self.getEdgeVisible(trees)
        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
            trees = []
            for line in content:
                trees.append(list(line))
            scores = []
            for col in range(1, len(trees)-1):
                for row in range(1, len(trees[0])-1):
                    scores.append(self.getViewDistance(trees, row, col))

        return max(scores)
