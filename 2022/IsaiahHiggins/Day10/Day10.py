#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script evaluation Day10

import sys
import os
from pathlib import Path

currentPath = os.path.dirname(os.path.abspath(__file__))
challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")
if challengePath not in sys.path:
   sys.path.append(challengePath)

import ChallengeBase


class Day10(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)
        self.currentCycle = 1
        self.reg = 1
        self._add_cycle = 2
        self._nop_cycle = 1
        self.screen = []
        self.currentPixle = -1
        self.width = 40

    def breakScreen(self):
        for i in range(0, len(self.screen), 40):
            yield self.screen[i:i+40]


    def  RunProgram(self, targetCycles, instruction):
        cycle_passed = False
        reg_val = 0
        parsed = instruction.split()
        if parsed[0] == 'noop':
            self.currentCycle += 1
            self.currentPixle = (self.currentPixle + 1) % self.width
            if self.reg == self.currentPixle or (self.reg - 1) == self.currentPixle or (self.reg + 1) == self.currentPixle:
                self.screen.append('#')
            else:
                self.screen.append(' ')
            if self.currentCycle in targetCycles:
                cycle_passed = True
                print("reg: ", self.reg, ", cycle: ", self.currentCycle)
                reg_val = self.reg * self.currentCycle
        else:
            for i in range(0, self._add_cycle):
                self.currentCycle += 1
                self.currentPixle = (self.currentPixle + 1) % self.width
                if self.reg == self.currentPixle or (self.reg - 1) == self.currentPixle or ((self.reg + 1) == self.currentPixle):
                    self.screen.append('#')
                else:
                    self.screen.append(' ')

                if i == self._add_cycle - 1:
                    self.reg += int(parsed[1])
                if self.currentCycle in targetCycles:
                    cycle_passed = True
                    print("reg: ", self.reg, ", cycle: ", self.currentCycle)
                    reg_val = self.reg * self.currentCycle
        return cycle_passed, reg_val



    def ExecuteP1(self, data: Path):
        answer = 0
        content = []
        #TODO implement evaluation
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
            print("part1 unevaluated")
            targets = list(range(20, 260, 40))
        instruction_count = 0
        while self.currentCycle < max(targets):
            cycle_passed, value = self.RunProgram(targets, content[instruction_count])
            instruction_count += 1
            if cycle_passed:
                print("target passed ", value)
                content[instruction_count - 1]
                answer += value


        return answer

    def ExecuteP2(self, data: Path):
        answer = []
        content = []
        #TODO implement evaluation
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        for line in content:
            cycle_passed, value = self.RunProgram([-2], line)
        display = self.breakScreen()
        for row in list(display):
            string = ""
            for char in row:
                string += char
            print(string)


        return "ASCII ART"
