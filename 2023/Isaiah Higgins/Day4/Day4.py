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
class Card():
    def __init__(self, id, input, answer):
        self.id = int(id)
        self.input = input.split()
        self.answer = answer.split()
        self.sum = 1

    def Get_Intersection(self):
        input = set(self.input)
        answer = set(self.answer)
        return input.intersection(answer)


class Day4(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)

    def ExecuteP1(self, data: Path):
        answer = 0
        content = []

        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]

        for line in content:
            id = int(line.split(":")[0].split()[1])
            content = line.split(":")[1]
            input = content.split("|")[0]
            tmp_answer = content.split("|")[1]
            card = Card(id, input, tmp_answer)
            matches = len(card.Get_Intersection())

            if matches > 0:
                answer += 2**(matches - 1)


        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        content = []

        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        cards = []
        for line in content:
            id = int(line.split(":")[0].split()[1])
            content = line.split(":")[1]
            input = content.split("|")[0]
            tmp_answer = content.split("|")[1]
            cards.append(Card(id, input, tmp_answer))

        for i in range(len(cards)):
            next_cards = len(cards[i].Get_Intersection())
            for j in range(i + 1, i + next_cards + 1):
                cards[j].sum += cards[i].sum

        for card in cards:
            answer += card.sum


        return answer
