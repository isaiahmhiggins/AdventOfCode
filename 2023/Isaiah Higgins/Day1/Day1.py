import regex as re
def part2Solution(lines):
    total=0
    for line in lines:
        nums=re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        wordNums = {'one': "1",
                    'two': "2",
                    'three': "3",
                    'four': "4",
                    'five': "5",
                    'six': "6",
                    'seven': "7",
                    'eight': "8",
                    'nine': "9",
                   }

        if nums[0] in wordNums:
            firstNum=wordNums[nums[0]]
        else:
            firstNum=nums[0]

        if nums[-1] in wordNums:
            lastNum=wordNums[nums[-1]]
        else:
            lastNum=nums[-1]

        firstLast=firstNum+lastNum

        total+=int(firstLast)

    return total

content = []
with open("./Real_Input.txt", 'r') as file:
    content = file.readlines()

for i in range(len(content)):
    content[i] = content[i].strip()


print(part2Solution(content))

