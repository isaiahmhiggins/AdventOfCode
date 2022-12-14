namespace AdventofCode.Day14;

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
    return 0;
  }

  private static long DoPart1(IReadOnlyList<string> lines)
  {
    return 0;
  }

  
}