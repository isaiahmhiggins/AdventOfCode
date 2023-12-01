#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script evaluation Day12

import sys
import os
from pathlib import Path
import networkx as nx
from itertools import islice
import time
import matplotlib.pyplot as plt

currentPath = os.path.dirname(os.path.abspath(__file__))
challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")
if challengePath not in sys.path:
   sys.path.append(challengePath)

import ChallengeBase


class Day12(ChallengeBase.Challenge.Challenge):

    def __init__(self, inputData: Path):
        super().__init__(inputData)
        self.map = []
        self.Graph = nx.DiGraph()
        self.startName = 0
        self.endName = 0
        self.pt2Starts = []

    def FillMap(self, content):
        self.map.append([])
        name = 0
        for line in content:
            for char in line:
                value = 0
                if char == 'S':
                    value = int(ord('a') - 97)
                    self.startName = name
                elif char == 'E':
                    value = value = int(ord('z') - 97)
                    self.endName = name
                else:
                    value = int(ord(char) - 97)
                if value == 0:
                    self.pt2Starts.append(name)
                self.map[-1].append((name, value))
                name += 1
            self.map.append([])
        self.map = self.map[:-1]

    def Pt1Connections(self):
        edges = []
        self.Graph = nx.DiGraph()
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                cur_name, cur_val = self.map[row][col]


                # check top connection
                if row > 0:
                    top_name, top_val = self.map[row-1][col]
                    if top_val <= cur_val or top_val - cur_val == 1:
                        edges.append((cur_name, top_name))

                # check bottom connection
                if row < len(self.map) - 1:
                    bottom_name, bottom_val = self.map[row+1][col]
                    if bottom_val <= cur_val or bottom_val - cur_val == 1:
                        edges.append((cur_name, bottom_name))

                # check left connection
                if col > 0:
                    left_name, left_val = self.map[row][col - 1]
                    if left_val <= cur_val or left_val - cur_val == 1:
                        edges.append((cur_name, left_name))

                # check right connection
                if col < len(self.map[0]) - 1:
                    right_name, right_val = self.map[row][col + 1]
                    if right_val <= cur_val or right_val - cur_val == 1:
                        edges.append((cur_name, right_name))

            self.Graph.add_edges_from(edges)

    def k_shortest_path(self, source, target, k, weight=None):
        return list(islice(nx.shortest_simple_paths(self.Graph, source, target, weight='weight'), k))

    def getLenShortestPath(self, source, target):
        return len(self.k_shortest_path(source, target, 1)[0]) - 1


    def ExecuteP1(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        self.FillMap(content)
        self.Pt1Connections()
        answer = self.getLenShortestPath(self.startName, self.endName)


        return answer

    def ExecuteP2(self, data: Path):
        answer = 0
        content = []
        with open(data, "r") as challenge_data:
            content = [i.strip() for i in challenge_data.readlines()]
        self.FillMap(content)
        self.Pt1Connections()
        shortest = 1000
        for start in self.pt2Starts:
            try:
                cost = self.getLenShortestPath(start, self.endName)
                if cost < shortest:
                    shortest = cost
            except:
                continue
        answer = shortest

        return answer
