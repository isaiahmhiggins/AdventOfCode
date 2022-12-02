This is Isaiah Higgin's working challenge folder
 - Each challenge is solved by a class per challenge. Each class derives from the Challenge ABC. 
 - Each Challenge has a part1 and part2 virtual method (from the Challenge ABC) That they must override
 - The Solve_Challenge_CLI file is the main interface for adding/executing a challenge
    - It dynamically finds, imports, and executes each solution
    - It handles executing challenge parts along with getting the challenge sample and real input from the folder and passing it to the solution file.

