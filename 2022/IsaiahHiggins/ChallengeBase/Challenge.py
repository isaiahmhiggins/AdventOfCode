#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: base class for all daily challenges

import abc
from pathlib import Path
import os
import sys


class Challenge(abc.ABC):
    def __init__(self, inputData: Path):

        # override the inputData path
        if not inputData.exists():
            sys.exit(1)
        else:
            self.sample = os.path.join(inputData, "sample.txt")
            self.challenge1 = os.path.join(inputData, "part1.txt")
            self.challenge2 = os.path.join(inputData, "part2.txt")

    def GetSample(self):
        return self.sample

    def GetPart1(self):
        return self.challenge1

    def GetPart2(self):
        return self.challenge2

    @abc.abstractmethod
    def execute(cls, data):
        ...
