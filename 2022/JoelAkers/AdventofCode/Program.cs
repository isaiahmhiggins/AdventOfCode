using AdventofCode.Day2;

Console.WriteLine("Day 2");
//var file = "C:\\Users\\akers\\OneDrive\\Documents\\2022\\AdventOfCode\\AdventOfCode\\2022\\JoelAkers\\AdventofCode\\Day2\\PracticeData.txt";
var file = "C:\\Users\\akers\\OneDrive\\Documents\\2022\\AdventOfCode\\AdventOfCode\\2022\\JoelAkers\\AdventofCode\\Day2\\RealData.txt";

var solver = new Solver();
var result = solver.Solve(file);

Console.WriteLine($"Result is: {result}");