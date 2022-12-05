using AdventofCode.Day4;

Console.WriteLine("Day 4");
//var file = "C:\\Users\\akers\\OneDrive\\Documents\\2022\\AdventOfCode\\AdventOfCode\\2022\\JoelAkers\\AdventofCode\\Day4\\PracticeData.txt";
var file = "C:\\Users\\akers\\OneDrive\\Documents\\2022\\AdventOfCode\\AdventOfCode\\2022\\JoelAkers\\AdventofCode\\Day4\\RealData.txt";

var solver = new Solver();
var result = solver.Solve(file, 2);

Console.WriteLine($"Result is: {result}");