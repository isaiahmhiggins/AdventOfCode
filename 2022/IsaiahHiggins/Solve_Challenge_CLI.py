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
    if not args.folder.exists():
        sys.exit(1)

    answer = 0
    # import challenge evaluation module
    filePath = os.path.abspath(list(args.folder.glob("*.py"))[0])
    name = os.path.basename(filePath)[:-3]

    module = importlib.import_module(f'{name}.{name}')

    # instantiate an instance of the path
    class_ = getattr(module, name)
    script = class_(args.folder)

    # invoke the script to get the answer
    if args.eval == 'sample':
        answer = script.execute(script.GetSample())
    elif args.eval == 'part1':
        answer = script.execute(script.GetPart1())
    else:
        answer = script.execute(script.GetPart2())

    return answer
    


def SetupOpts():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--folder", help = "folder containing the challenge", type = Path,
    required=True, dest="folder")

    parser.add_argument("-e", "--eval", dest="eval", help="Which result to evaluate", choices = ["sample", "part1", "part2"], required=True)

    return parser


def main():
    parser  = SetupOpts()
    args = parser.parse_args()

    print(f"The answer is: {Evaluate_script(args)}")



    



if __name__ == "__main__":
    main()