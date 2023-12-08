import copy
from dataclasses import dataclass
import math


day_number = str(6)
sample_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_1.txt"
real_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_1.txt"
sample_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_2.txt"
real_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_2.txt"

IS_DEBUG = True



class Race:
    time: int
    distance: int

    def __init__(self, time: int, dist: int) -> None:
        self.time = time
        self.distance = dist
    
    def get_distance(self, time_held: int):
        return (self.time - time_held) * time_held
    
    def did_beat(self, time_held: int) -> bool:
        return self.get_distance(time_held) > self.distance

    def get_ideal_time(self) -> float:
        return self.time / 2
    
class RaceCollection1:
    races: dict[int, Race] = {}

    def __init__(self, lines: list[str]) -> None:
        time_colon_split = lines[0].split(':')
        dist_colon_split = lines[1].split(':')

        times = [int(number.strip()) for number in time_colon_split[1].split(' ') if len(number) > 0]
        distance = [int(number.strip()) for number in dist_colon_split[1].split(' ') if len(number) > 0]
        for i in range(len(times)):
            self.races[i] = Race(times[i], distance[i])
        
class RaceCollection2:
    races: dict[int, Race] = {}

    def __init__(self, lines: list[str]) -> None:
        time_colon_split = lines[0].split(':')
        dist_colon_split = lines[1].split(':')

        times = [int(time_colon_split[1].replace(' ','').strip())]
        distance = [int(dist_colon_split[1].replace(' ','').strip())]

        for i in range(len(times)):
            self.races[i] = Race(times[i], distance[i])
        

def solution_part_1():
    with open(real_1, 'r') as open_file:
        lines = [line.strip() for line in open_file.readlines()]
        race_collection = RaceCollection1(lines)
        total_values = 1
        for race in race_collection.races.values():
            ideal_time = race.get_ideal_time()
            is_whole = True
            if ideal_time - int(ideal_time) != 0:
                ideal_time = int(ideal_time)
                is_whole = False
            holding_time_shorter = copy.copy(ideal_time)
            holding_time_longer = copy.copy(ideal_time)

            while race.did_beat(holding_time_shorter) and race.did_beat(holding_time_longer):
                holding_time_shorter -= 1
                holding_time_longer += 1 
            
            possible_wins = (ideal_time - holding_time_shorter) * 2
            if is_whole:
                possible_wins -= 1
            if IS_DEBUG:
                print(f"Race: time {race.time}, winning dist {race.distance}, possible wins {possible_wins}")
            total_values *= possible_wins
        
        print("Total: " + str(total_values))
                

def solution_part_2():
    with open(real_1, 'r') as open_file:
        lines = [line.strip() for line in open_file.readlines()]
        race_collection = RaceCollection2(lines)
        total_values = 1
        for race in race_collection.races.values():
            ideal_time = race.get_ideal_time()
            is_whole = True
            if ideal_time - int(ideal_time) != 0:
                ideal_time = int(ideal_time)
                is_whole = False
            holding_time_shorter = copy.copy(ideal_time)
            holding_time_longer = copy.copy(ideal_time)

            while race.did_beat(holding_time_shorter) and race.did_beat(holding_time_longer):
                holding_time_shorter -= 1
                holding_time_longer += 1 
            
            possible_wins = (ideal_time - holding_time_shorter) * 2
            if is_whole:
                possible_wins -= 1
            if IS_DEBUG:
                print(f"Race: time {race.time}, winning dist {race.distance}, possible wins {possible_wins}")
            total_values *= possible_wins
        
        print("Total: " + str(total_values))


solution_part_2()