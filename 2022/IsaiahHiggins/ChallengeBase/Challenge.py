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
            self.real = os.path.join(inputData, "real.txt")

    def GetSample(self):
        return self.sample

    def GetReal(self):
        return self.real


    @abc.abstractmethod
    def ExecuteP1(cls, data):
        ...

    @abc.abstractmethod
    def ExecuteP2(cls, data):
        ...
