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

class Draw():
    def __init__(self, red, blue, green):
        self.red = red
        self.blue = blue
        self.green = green

    def __repr__(self):
        return f"red: {self.red}, green: {self.green}, blue: {self.blue}"

class Game():
    def __init__ (self, id, draws: list):
        self.id = id
        self.draws = draws

    def __repr__(self):
        string = f"ID: {self.id}\n"
        for draw in self.draws:
            string += str(draw) + "\n"
        return string


class Day2(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)

    def ParseInput(self, lines):
        games = []
        # Go over each game
        for line in lines:
            gameplay = line.split(':')[1]
            id = line.split(':')[0].split(" ")[1]

            # go through each draw
            data = []
            for draw in gameplay.split(";"):
                # go through each catagory
                red = 0
                blue = 0
                green = 0
                for color in draw.split(','):
                    if color.split()[1] == "red":
                        red = color.split()[0]
                    elif color.split()[1] == "green":
                        green = color.split()[0]
                    else:
                        blue = color.split()[0]
                data.append(Draw(int(red), int(blue), int(green)))
            games.append(Game(id, data))
        return games


    def ExecuteP1(self, data: Path):
        answer = 0
        content = []

        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        input = self.ParseInput(content)
        red_max = 12
        green_max = 13
        blue_max = 14

        for game in input:
            game_good = True
            for round in game.draws:
                if round.red > red_max or round.green > green_max or round.blue > blue_max:
                    game_good = False
                    break
            if game_good:
                print(game.id)
                answer += int(game.id)

        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]

        input = self.ParseInput(content)

        for game in input:
            red = []
            green = []
            blue = []
            for draw in game.draws:
                red.append(draw.red)
                green.append(draw.green)
                blue.append(draw.blue)
            r_max = max(red)
            g_max = max(green)
            b_max = max(blue)
            answer += r_max * g_max * b_max

        return answer
