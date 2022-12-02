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

    def convertOpponentToStandard(self, opponentMove: str) -> str:
        """Converts opponent move to rock, paper, or scissors"""
        convertDict = {"A": "Rock", "B": "Paper", "C": "scissors"}
        return convertDict[opponentMove]

    def convertSelfToStandard(self, selfMove: str) -> str:
        """Converts opponent move to rock, paper, or scissors"""
        convertDict = {"X": "Rock", "Y": "Paper", "Z": "scissors"}
        return convertDict[selfMove]

    def getMoveScore(self, move):
        """Converts move into score"""
        convertDict = {"Rock": 1, "Paper": 2, "scissors": 3}
        return convertDict[move]

    def GetWinnerScore(self, opponentMove: str, youMove: str) -> int:
        """Returns victory score if you win, false otherwise"""
        score = 0
        opponentMove = self.convertOpponentToStandard(opponentMove)
        youMove = self.convertSelfToStandard(youMove)
        # check tie
        if (youMove == opponentMove):
            score = 3
        # check win
        elif(youMove == "Rock" and opponentMove == "scissors"):
            score = 6
        elif((youMove == "Paper") and (opponentMove == "Rock")):
            score = 6
        elif(youMove == "scissors" and opponentMove == "Paper"):
            score = 6
        return score

    def GetWinningMove(self, opponentMove):
        # ROCK A, PAPER B, scissors, C
        # ROCK X, PAPER Y, scissors, Z
        winningMoves = {"A": "Y", "B": "Z", "C": "X"}
        return winningMoves[opponentMove]


    def GetLosingMove(self, opponentMove):
        loesingMoves = {"A": "Z", "B": "X", "C": "Y"}
        return loesingMoves[opponentMove]

    def GetMove(self, opponentMove, outcome):
        moveDict = {"X": "lose", "Y": "tie", "Z": "Win"}
        tieDict = {"A": "X", "B": "Y", "C": "Z"}
        outcome = moveDict[outcome]
        move = ""
        if outcome == "Win":
            move = self.GetWinningMove(opponentMove)
        elif outcome == "lose":
            move = self.GetLosingMove(opponentMove)
        else:
            move = tieDict[opponentMove]
        return move


    def ExecuteP1(self, data: Path):
        answer = 0
        with open(data, "r") as challenge_data:
            content = challenge_data.readlines()
            content = [i.strip() for i in content]
            for play in content:
                opponent, myMove = play.split()
                answer += (self.getMoveScore(self.convertSelfToStandard(myMove)) + self.GetWinnerScore(opponent, myMove))

        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        with open(data, "r") as challenge_data:
            content = challenge_data.readlines()
            content = [i.strip() for i in content]
            for play in content:
                oppenent, outcome = play.split()
                myMove = self.GetMove(oppenent, outcome)
                answer += (self.getMoveScore(self.convertSelfToStandard(myMove)) + self.GetWinnerScore(oppenent, myMove))
        return answer
