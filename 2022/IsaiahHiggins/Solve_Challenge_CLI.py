#! usr/bin/env python3.10
# Author: Isaiah Higgins
# Date: 11/19/2022
# Description: test script to make sure that the CLI can import correctly
import argparse
from pathlib import Path
import importlib
import sys
import os
import glob
from ChallengeBase.Challenge import Challenge


def Evaluate_script(args) -> int:
    # check for correct folder
    args.folder = Path(os.path.abspath(args.folder))
    print(args.folder)
    if not args.folder.exists():
        sys.exit(1)

    answer = 0
    # import challenge evaluation module
    filePath = os.path.abspath(list(args.folder.glob("*.py"))[0])
    module_name = os.path.basename(filePath)[:-3]

    module = importlib.import_module(f'{module_name}.{module_name}')

    # instantiate an instance of the path
    class_ = getattr(module, module_name)
    script = class_(args.folder)

    # invoke the script to get the answer
    data = ""
    if args.eval == 'sample':
        data = script.GetSample()
    elif args.eval == 'real':
        data = script.GetReal()

    if args.part == 'part1':
        answer = script.ExecuteP1(data)
    elif args.part == 'part2':
        answer = script.ExecuteP2(data)

    return answer


def New_Challenge(challenge_name: str):
    fileContent = ('#! usr/bin/env python3.10\r\n'
    '# Author: Isaiah Higgins\r\n'
    '# Date: 11/19/2022\r\n'
    '# Description: test script evaluation {name}\r\n'
    '\r\n'
    'import sys\r\n'
    'import os\r\n'
    'from pathlib import Path\r\n'
    '\r\n'
    'currentPath = os.path.dirname(os.path.abspath(__file__))\r\n'
    'challengePath = os.path.join(os.path.dirname(currentPath), "ChallengeBase")\r\n'
    'if challengePath not in sys.path:\r\n'
    '   sys.path.append(challengePath)\r\n'
    '\r\n'
    'import ChallengeBase\r\n'
    '\r\n'
    '\r\n'
    'class {name}(ChallengeBase.Challenge.Challenge):\r\n'
    '\r\n'
    '    def __init__(self, inputData: Path):\r\n'
    '        super().__init__(inputData)\r\n'
    '\r\n'
    '    def ExecuteP1(self, data: Path):\r\n'
    '        answer = 0\r\n'
    '        content = []\r\n'
    '        #TODO implement evaluation\r\n'
    '        with open(data, "r") as challenge_data:\r\n'
    '            print("part1 unevaluated")\r\n'
    '        return answer\r\n'
    '\r\n'
    '    def ExecuteP2(self, data: Path):\r\n'
    '        answer = 0\r\n'
    '        content = []\r\n'
    '        #TODO implement evaluation\r\n'
    '        with open(data, "r") as challenge_data:\r\n'
    '            print("part2 unevaluated")\r\n'
    '        return answer\r\n')

    currentPath = os.path.dirname(os.path.abspath(__file__))
    newFolder = os.path.join(currentPath, challenge_name)
    if not os.path.exists(newFolder):
        os.mkdir(newFolder)

    with open(os.path.join(newFolder, f"{challenge_name}.py"), 'w') as pythonFile:
        pythonFile.write(fileContent.format_map({"name": challenge_name}))

    with open(os.path.join(newFolder, "sample.txt"), "w") as sampleInput:
        sampleInput.write("")

    with open(os.path.join(newFolder, "real.txt"), "w") as sampleInput:
        sampleInput.write("")


def SetupOpts():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help = 'run or create a script', dest = 'command')

    evaluate_parse = subparsers.add_parser('run', help='Run a challenge evaluator')
    evaluate_parse.add_argument("-f", "--folder", help = "folder containing the challenge", type = Path,
    required=True, dest="folder")

    evaluate_parse.add_argument("-e", "--eval", dest="eval", help="Which result to evaluate", choices = ["sample", "real"], required=True)

    evaluate_parse.add_argument("-p", "--part", dest="part", choices= ['part1', 'part2'], help= "which part of the challenge to perform")

    new_script = subparsers.add_parser('new', help='create a new evaluation script')
    new_script.add_argument("-n", "--name", help='name of the script/class/folder', required=True)

    return parser


def main():
    parser  = SetupOpts()
    args = parser.parse_args()

    if args.command == 'new':
        New_Challenge(args.name)

    if args.command == 'run':
        print(f"The answer is: {Evaluate_script(args)}")







if __name__ == "__main__":
    main()