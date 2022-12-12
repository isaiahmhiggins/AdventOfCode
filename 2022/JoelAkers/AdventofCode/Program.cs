using AdventofCode.Day11;

Console.WriteLine("Day 11");
//var file = "C:\\Users\\akers\\OneDrive\\Documents\\2022\\AdventOfCode\\AdventOfCode\\2022\\JoelAkers\\AdventofCode\\Day11\\PracticeData.txt";
var file = "C:\\Users\\akers\\OneDrive\\Documents\\2022\\AdventOfCode\\AdventOfCode\\2022\\JoelAkers\\AdventofCode\\Day11\\RealData.txt";

var now = DateTime.Now;
var solver = new Solver();
solver.Solve(file, 2);
var after = DateTime.Now;
Console.WriteLine($"\nTime Taken: {after - now}");