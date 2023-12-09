import copy
from dataclasses import dataclass
from enum import Enum
import math


day_number = str(7)
sample_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_1.txt"
real_1 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_1.txt"
sample_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\sample_2.txt"
real_2 = f".\\AdventOfCode\\2023\\Joel Akers\\day_{day_number}\\real_2.txt"

IS_DEBUG = True

card_to_value1 = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

card_to_value2 = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1,
}
class HandTypes(Enum):
    Five = 7
    Four = 6
    Full = 5
    Three = 4
    Two = 3
    One = 2
    High = 1

class Hand1:
    cards: list[str] = []
    bid: int
    def __init__(self, hand: str, bid: int) -> None:
        self.cards = [char for char in hand.strip()]
        self.bid = bid
    
    def get_type(self) -> HandTypes:
        # if all([card == self.cards[0] for card in self.cards]):
        #     return HandTypes.Five
        hand_dict = {}
        for card in self.cards:
            card_value = card_to_value1[card]
            if card_value in hand_dict.keys():
                hand_dict[card_value] += 1
                continue
            hand_dict[card_value] = 1
        if any([hand_dict[value] == 5 for value in hand_dict.keys()]):
            return HandTypes.Five
        if any([hand_dict[value] == 4 for value in hand_dict.keys()]):
            return HandTypes.Four
        if any([hand_dict[value] == 3 for value in hand_dict.keys()]) \
            and any([hand_dict[value] == 2 for value in hand_dict.keys()]):
            return HandTypes.Full
        if any([hand_dict[value] == 3 for value in hand_dict.keys()]):
            return HandTypes.Three
        if len([True for value in hand_dict.keys() if hand_dict[value] == 2]) == 2:
            return HandTypes.Two
        if len([True for value in hand_dict.keys() if hand_dict[value] == 2]) == 1:
            return HandTypes.One
        if all([hand_dict[value] == 1 for value in hand_dict.keys()]):
            return HandTypes.High
        print("This Hand somehow has no type: " + ''.join(self.cards))
        
    def __lt__(self, obj: object) -> bool:
        assert isinstance(obj, Hand1)
        this_hand_type_value = self.get_type().value
        other_hand_type_value = obj.get_type().value

        if this_hand_type_value < other_hand_type_value:
            return True
        if this_hand_type_value > other_hand_type_value:
            return False
        for i in range(len(self.cards)):
            if card_to_value1[self.cards[i]] == card_to_value1[obj.cards[i]]:
                continue
            return card_to_value1[self.cards[i]] < card_to_value1[obj.cards[i]]
        return False
        
    def __eq__(self, __value: object) -> bool:
        assert isinstance(__value, Hand1)
        return not (self < __value) and not (__value < self)


class Hand2:
    cards: list[str] = []
    bid: int
    _type: HandTypes
    cards_value: int
    def __init__(self, hand: str, bid: int) -> None:
        self.cards = [char for char in hand.strip()]
        self.bid = bid
        self._type = self.get_type()
        if IS_DEBUG:
            print(f"Hand {hand} is a {str(self._type)}")
    
    @property
    def type(self) -> HandTypes:
        return self._type

    def get_type(self) -> HandTypes:
        # if all([card == self.cards[0] for card in self.cards]):
        #     return HandTypes.Five
        hand_dict = {}
        jack_count = 0
        for card in self.cards:
            if card == 'J':
                jack_count += 1
                continue
            card_value = card_to_value2[card]
            if card_value in hand_dict.keys():
                hand_dict[card_value] += 1
                continue
            hand_dict[card_value] = 1
        if any([hand_dict[value] + jack_count == 5 for value in hand_dict.keys()]) or jack_count == 5:
            # 11111, 1111J, 111JJ, 11JJJ, 1JJJJ, JJJJJ
            return HandTypes.Five
        if any([hand_dict[value] + jack_count  == 4 for value in hand_dict.keys()]):
            # 12222, 1222J, 122JJ, 12JJJ
            return HandTypes.Four
        if any([hand_dict[value] == 3 for value in hand_dict.keys()]) \
            and any([hand_dict[value] == 2 for value in hand_dict.keys()]):
            # 11222
            return HandTypes.Full
        if any([hand_dict[value] + jack_count == 3 for value in hand_dict.keys()]):
            if len([True for value in hand_dict.keys() if hand_dict[value] == 2]) == 2 and jack_count == 1:
                # 1122J
                return HandTypes.Full
            # 12333, 1233J, 123JJ
            return HandTypes.Three
        if len([True for value in hand_dict.keys() if hand_dict[value] == 2]) == 2:
            # 11223
            return HandTypes.Two
        if len([True for value in hand_dict.keys() if hand_dict[value] == 2]) == 1 or jack_count == 1:
            # 11234, 1J234
            return HandTypes.One
        if all([hand_dict[value] == 1 for value in hand_dict.keys()]):
            # 12345
            return HandTypes.High
        print("This Hand somehow has no type: " + ''.join(self.cards))
        
    def __lt__(self, obj: object) -> bool:
        assert isinstance(obj, Hand2)
        this_hand_type_value = self.type.value
        other_hand_type_value = obj.type.value

        if this_hand_type_value < other_hand_type_value:
            return True
        if this_hand_type_value > other_hand_type_value:
            return False
        for i in range(len(self.cards)):
            if card_to_value2[self.cards[i]] == card_to_value2[obj.cards[i]]:
                continue
            return card_to_value2[self.cards[i]] < card_to_value2[obj.cards[i]]
        return False
        
    def __eq__(self, __value: object) -> bool:
        assert isinstance(__value, Hand2)
        return not (self < __value) and not (__value < self)

class ParsedFile1:
    hands: list[Hand1] = []
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            split_line = line.split(' ')
            self.hands.append(Hand1(split_line[0].strip(), int(split_line[1].strip())))


class ParsedFile2:
    hands: list[Hand2] = []
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            split_line = line.split(' ')
            self.hands.append(Hand2(split_line[0].strip(), int(split_line[1].strip())))

def solution_part_1():
    with open(real_1, 'r') as open_file:
        lines = [line.strip() for line in open_file.readlines()]
        parsed_file = ParsedFile1(lines)
        total_value = 0
        parsed_file.hands.sort()
        for i in range(len(parsed_file.hands)):
            total_value += parsed_file.hands[i].bid * (i + 1)
        print("Total: " + str(total_value))
                

def solution_part_2():
    with open(real_1, 'r') as open_file:
        lines = [line.strip() for line in open_file.readlines()]
        parsed_file = ParsedFile2(lines)
        total_value = 0
        parsed_file.hands.sort()
        for i in range(len(parsed_file.hands)):
            total_value += parsed_file.hands[i].bid * (i + 1)
        print("Total: " + str(total_value))
        


solution_part_2()