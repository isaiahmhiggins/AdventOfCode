using AdventofCode.Day3;

Console.WriteLine("Day 3");
//var file = "C:\\Users\\akers\\OneDrive\\Documents\\2022\\AdventOfCode\\AdventOfCode\\2022\\JoelAkers\\AdventofCode\\Day3\\PracticeData.txt";
var file = "C:\\Users\\akers\\OneDrive\\Documents\\2022\\AdventOfCode\\AdventOfCode\\2022\\JoelAkers\\AdventofCode\\Day3\\RealData.txt";

var solver = new Solver();
var result = solver.Solve(file, 2);

Console.WriteLine($"Result is: {result}");