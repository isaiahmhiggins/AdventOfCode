from copy import deepcopy
word_to_digit = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0
    }

def day_1_part_1():
    with open("./day_1/input_1.txt", 'r') as open_file:
        lines = open_file.readlines()
        value = 0
        for line in lines:
            digits = [letter for letter in line if letter.isdigit()]
            next_digit = int(digits[0]) * 10 + int(digits[-1])
            value += next_digit
            print(f"sum: {next_digit}")
        print("total: " + str(value))


def day_1_part_2():
    
    expected_values = iter([29, 83, 13, 24, 42, 14, 76])
    with open("./day_1/input_1.txt", 'r') as open_file:
        lines = open_file.readlines()
        value = 0
        for line in lines:
            line_for_first_match = deepcopy(line)
            line_for_last_match = deepcopy(line)

            best_first_match = (100, 100) # index, value
            for i in range(len(line_for_first_match)):
                if line_for_first_match[i].isdigit():
                    best_first_match = (i, int(line_for_first_match[i]))
                    break
            word_matches = [(line_for_first_match.find(word), word) for word in word_to_digit.keys()]
            for index, word in word_matches:
                if index >= 0 and index < best_first_match[0]:
                    best_first_match = (index, word_to_digit[word])
                    
            
            best_last_match = (-1, -1) # index, value
            for i in range(len(line_for_last_match)):
                index = len(line_for_last_match) - 1 - i
                if line_for_last_match[index].isdigit():
                    best_last_match = (index, int(line_for_last_match[index]))
                    break
            word_matches = [(line_for_last_match.rfind(word), word) for word in word_to_digit.keys()]
            for index, word in word_matches:
                if index >= 0 and index > best_last_match[0]:
                    best_last_match = (index, word_to_digit[word])
            next_digit = best_first_match[1] * 10 + best_last_match[1]
            value += next_digit
            print(f"original: {line.strip()}; modified: {line_for_first_match.strip()}; result: {next_digit}")

        print("total: " + str(value))


day_1_part_2()