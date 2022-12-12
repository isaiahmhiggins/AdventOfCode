using System.Numerics;

namespace AdventofCode.Day12;

public class Solver
{
  public void Solve(string filePath, int partNumber)
  {
    var fileLines = File.ReadAllLines(filePath).ToList();
    var result = partNumber switch
    {
      2 => DoPart2(fileLines),
      1 => DoPart1(fileLines),
      _ => throw new ArgumentOutOfRangeException(nameof(partNumber), partNumber, null)
    };
    Console.Write($"Result is: {result}");
  }

  private static long DoPart2(IReadOnlyList<string> lines)
  {
    var mapper = new Mapper2(lines);
    var finalPoint = mapper.FindPath();
    mapper.PrintMap(finalPoint);
    var currentPoint = finalPoint;
    var steps = 0;
    while (currentPoint.Parent != null)
    {
      steps++;
      currentPoint = currentPoint.Parent;
    }
    return steps;
  }

  private static long DoPart1(IReadOnlyList<string> lines)
  {
    var mapper = new Mapper(lines);
    var finalPoint = mapper.FindPath();
    mapper.PrintMap(finalPoint);
    var currentPoint = finalPoint;
    var steps = 0;
    while (currentPoint.Parent != null)
    {
      steps++;
      currentPoint = currentPoint.Parent;
    }
    return steps;
  }
  
}