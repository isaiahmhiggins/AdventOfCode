#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script evaluation Day7

import sys
import os
from pathlib import Path

currentPath = os.path.dirname(os.path.abspath(__file__))
challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")
if challengePath not in sys.path:
   sys.path.append(challengePath)

import ChallengeBase

class file:
    def __init__(self, size, name):
        self.size = size
        self.name = name

class directory:
    def __init__(self, name, parent):
        self.subdirs = []
        self.files = []
        self.name = name
        self.parent = parent

    def getSize(self):
        size = 0
        for file in self.files:
            size += file.size
        for dir in self.subdirs:
            size += dir.getSize()
        return size

class Day7(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)
        self.directories = []
        self.currentDirectoryIndex = 0

    def handleCD(self, directoryName):
        directoryNames = [i.name for i in self.directories]
        # handle if home directory
        if directoryName not in directoryNames and directoryName != '..':
            self.directories.append(directory(directoryName, None))
            directoryNames = [i.name for i in self.directories]

        # handle going back a directory
        elif directoryName == '..':
            parentDir = self.directories[self.currentDirectoryIndex].parent
            self.currentDirectoryIndex = self.directories.index(parentDir)

        else:
            subdirNames = [i.name for i in self.directories[self.currentDirectoryIndex].subdirs]

            subdir = self.directories[self.currentDirectoryIndex].subdirs[subdirNames.index(directoryName)]
            self.currentDirectoryIndex = self.directories.index(subdir)


    def handleLS(self, content):
        for i in range(0, len(content), 2):
            if content[i] == 'dir':
                newDir = directory(content[i+1], self.directories[self.currentDirectoryIndex])
                self.directories.append(newDir)
                self.directories[self.currentDirectoryIndex].subdirs.append(newDir)
            else:
                newFile = file(int(content[i]), content[i+1])
                self.directories[self.currentDirectoryIndex].files.append(newFile)

    def ExecuteP1(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = challenge_data.read()
            # remove newlines
            content = content.replace('\n', ' ')
            # sepearate all commands
            content = content.split('$')
            # remove any stray lines
        for count, line in enumerate(content):
            # get command parts
            if line != "":
                command = line.split()
                if command[0] == 'cd':
                    self.handleCD(command[1])
                elif command[0] == 'ls':
                    self.handleLS(command[1:])


        sizes = []
        for dir in self.directories:
            size = dir.getSize()
            if size < 100000:
                answer += size

        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        self.ExecuteP1(data)
        totalDisk = 70000000
        target = 30000000

        free = totalDisk - self.directories[0].getSize()
        remaining = target - free
        candidates = []
        for dir in self.directories:
            size = dir.getSize()
            if size >= remaining:
                candidates.append(size)
        print(candidates)
        answer = min(candidates)

        return answer
