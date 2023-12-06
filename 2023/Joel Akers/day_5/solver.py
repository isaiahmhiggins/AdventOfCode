import copy
from dataclasses import dataclass
import math


day_number = str(5)
sample_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_1.txt"
real_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_1.txt"
sample_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_2.txt"
real_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_2.txt"

class Range:
    starting_value: int
    count: int
    ending_value: int

    def __init__(self, starting_value: int, count: int):
        self.starting_value =  starting_value
        self.count =  count
        self.ending_value =  starting_value + count - 1

    def subtract_range(self, a: 'Range') -> list['Range']:
        # a starts before and ends in middle
        if a.starting_value <= self.starting_value <= a.ending_value <= self.ending_value:
            return [Range(a.ending_value, self.ending_value - a.ending_value + 1)]
        # a starts in middle and runs off end
        if self.starting_value <= a.starting_value <= self.ending_value <= a.ending_value:
            return [Range(self.starting_value, a.starting_value - self.starting_value + 1)]
        # a starts before and ends before
        if a.ending_value < self.starting_value:
            return [Range(self.starting_value, self.count)]
        # a starts before and ends after end
        if a.starting_value <= self.starting_value and a.ending_value >= self.ending_value:
            return []
        # a starts in middle and ends in middle
        if self.starting_value <= a.starting_value <= a.ending_value <= self.ending_value:
            return [
                Range(self.starting_value, a.starting_value - self.starting_value + 1),
                Range(a.ending_value + 1, self.ending_value + 1)
            ]
        # a starts after end and ends after end
        if self.ending_value <= a.starting_value:
            return [Range(self.starting_value, self.count)]

    def contains_value(self, value: int) -> bool:
        return self.starting_value <= value <= self.ending_value

    def overlaps(self, input_range: 'Range') -> bool:
        if self.starting_value <= input_range.ending_value <= self.ending_value:
            return True
        if input_range.starting_value <= self.starting_value <= input_range.ending_value:
            return True
        return False

    
def value_in_range(input_value: int, range_a: Range) -> bool:
    return range_a.starting_value <= input_value <= range_a.ending_value


class Seeds2:
    values: list[Range] = []
    def __init__(self, line: str):
        numbers_string = line.split(':')[1].strip()
        numbers = [int(number) for number in numbers_string.split(' ')]
        for i in range(0, len(numbers), 2):
            self.values.append(Range(numbers[i], numbers[i+1]))


class Seeds1:
    values: list[int]
    def __init__(self, line: str):
        numbers_string = line.split(':')[1].strip()
        self.values = [int(number) for number in numbers_string.split(' ')]

class ResourceMapper:
    source_category: str
    destination_category: str

    def __init__(self, lines: list[str]) -> None:
        space_split = lines[0].split(' ')
        dash_split = space_split[0].split('-')
        self.source_category = dash_split[0].strip()
        self.destination_category = dash_split[2].strip()
        self._source_points_to_destination_points = {}
        self._source_points_to_ranges = {}
        self._source_start_to_dest_range: dict[int, Range] = {}
        for i in range(1, len(lines)):
            space_split = lines[i].split(' ')
            resource_range = int(space_split[2].strip())
            destination_start = int(space_split[0].strip())
            source_start = int(space_split[1].strip())
            self._source_start_to_dest_range[source_start] = Range(destination_start, resource_range)
            self._source_points_to_destination_points[source_start] = destination_start
            self._source_points_to_ranges[source_start] = resource_range

    def translate_value(self, key: int) -> int:
        for start_point in self._source_points_to_destination_points.keys():
            if key >= start_point and key < start_point + self._source_points_to_ranges[start_point]:
                relative_move = key - start_point
                dest_start = self._source_points_to_destination_points[start_point]
                return dest_start + relative_move
        return key

    def translate_range(self, range_input: Range) -> list[Range]:
        min_sources = [key for key in self._source_start_to_dest_range.keys()]
        min_sources.sort()
        resulting_ranges: list[Range] = []
        i = range_input.starting_value
        while i <= range_input.ending_value and len(min_sources) > 0:
            next_range = Range(min_sources[0], self._source_start_to_dest_range[min_sources[0]].count)
            # There is a range of non-transformed values before the minimum transformer
            if i < next_range.starting_value:
                ending_value = min(next_range.starting_value - 1, range_input.ending_value)
                resulting_ranges.append(Range(i, ending_value - i + 1))
                i = ending_value + 1
                continue
            # a filter range is the start of a next range
            if i == next_range.starting_value:
                ending_value = min(next_range.ending_value, range_input.ending_value)
                resulting_range_count = ending_value - i + 1
                resulting_ranges.append(Range(self._source_start_to_dest_range[next_range.starting_value].starting_value, resulting_range_count))
                i = ending_value + 1
                min_sources.pop(0)
                continue
            # a filter range starts before the range input but extends through range input
            if next_range.starting_value < i < next_range.ending_value:
                ending_value = min(next_range.ending_value, range_input.ending_value)
                resulting_range_count = ending_value - i + 1
                range_start = self._source_start_to_dest_range[next_range.starting_value].starting_value + i - next_range.starting_value
                resulting_ranges.append(Range(range_start, resulting_range_count))
                i = ending_value + 1
                min_sources.pop(0)
                continue
            if next_range.ending_value < i:
                min_sources.pop(0)
                continue
        # range input extends past any filter ranges existing
        if i <= range_input.ending_value:
            resulting_ranges.append(Range(i, range_input.ending_value - i + 1))
        return resulting_ranges

def solution_part_1():
    with open(real_1, 'r') as open_file:
        lines = [line.strip() for line in open_file.readlines()]
        seeds = Seeds1(lines[0])
        resource_mappings: dict[str, ResourceMapper] = {}
        next_resource_mapping_lines = []
        i = 2
        while i <= len(lines):
            if i < len(lines) and not len(lines[i]) <= 1:
                next_resource_mapping_lines.append(lines[i])
            else:
                next_resource_mapper = ResourceMapper(next_resource_mapping_lines)
                resource_mappings[next_resource_mapper.source_category] = next_resource_mapper
                next_resource_mapping_lines = []
            i += 1

        closest_location = 100000000000
        for seed in seeds.values:
            #linked_str = ''
            starting_resource = 'seed'
            ending_resource = 'location'
            resource_mapping = resource_mappings[starting_resource]
            cur_value = seed
            while resource_mapping.destination_category != ending_resource:
                #linked_str += f"{resource_mapping.source_category} {cur_value}, "
                cur_value = resource_mapping.translate_value(cur_value)
                resource_mapping = resource_mappings[resource_mapping.destination_category]
            location_value = resource_mapping.translate_value(cur_value)
            #linked_str += f"{resource_mapping.destination_category} {location_value}"
            #print(linked_str)
            #print('Found Location: ' + str(location_value) + ' from seed ' + str(seed))
            if location_value < closest_location:
                closest_location = location_value
        print('Closest: ' + str(closest_location))

IS_DEBUG = False
def solution_part_2():
    with open(real_1, 'r') as open_file:
        lines = [line.strip() for line in open_file.readlines()]
        seeds = Seeds2(lines[0])
        resource_mappings: dict[str, ResourceMapper] = {}
        next_resource_mapping_lines = []
        i = 2
        while i <= len(lines):
            if i < len(lines) and not len(lines[i]) <= 1:
                next_resource_mapping_lines.append(lines[i])
            else:
                next_resource_mapper = ResourceMapper(next_resource_mapping_lines)
                resource_mappings[next_resource_mapper.source_category] = next_resource_mapper
                next_resource_mapping_lines = []
            i += 1

        closest_location = 100000000000
        for seed_start in seeds.values:
            linked_str = ''
            starting_resource = 'seed'
            ending_resource = 'location'
            resource_mapping = resource_mappings[starting_resource]
            cur_value = [seed_start]
            while resource_mapping.destination_category != ending_resource:
                if IS_DEBUG:
                    linked_str += f"{resource_mapping.source_category} {cur_value}, "
                next_value = []
                for item in cur_value:
                    next_value.extend(resource_mapping.translate_range(item))
                resource_mapping = resource_mappings[resource_mapping.destination_category]
                cur_value = next_value
            for item in cur_value:
                location_value = min([i.starting_value for i in resource_mapping.translate_range(item)])
                if IS_DEBUG:
                    linked_str += f"{resource_mapping.destination_category} {location_value}"
                    print(linked_str)
                    print('Found Location: ' + str(location_value) + f' from seed range {seed_start.starting_value}-{seed_start.ending_value}')
                if location_value < closest_location:
                    closest_location = location_value
        print('Closest: ' + str(closest_location))


solution_part_2()