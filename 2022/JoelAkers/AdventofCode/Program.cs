using AdventofCode.Day14;

var day = "Day14";
Console.WriteLine(day);
var practiceFile = $"C:\\Users\\akers\\OneDrive\\Documents\\2022\\AdventOfCode\\AdventOfCode\\2022\\JoelAkers\\AdventofCode\\{day}\\PracticeData.txt";
var file = $"C:\\Users\\akers\\OneDrive\\Documents\\2022\\AdventOfCode\\AdventOfCode\\2022\\JoelAkers\\AdventofCode\\{day}\\RealData.txt";

var now = DateTime.Now;
var solver = new Solver();
solver.Solve(practiceFile, 1);
var after = DateTime.Now;
Console.WriteLine($"\nTime Taken: {after - now}");
