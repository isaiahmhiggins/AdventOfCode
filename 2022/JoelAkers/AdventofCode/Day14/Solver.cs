namespace AdventofCode.Day14;

public class Solver
{
  private bool _isDebug = false;
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

  private long DoPart2(IReadOnlyList<string> lines)
  {
    var sandyCave = new SandyCave(lines, 500, 0, false);
    var totalDropped = 0;
    while (sandyCave.DropSandUnit())
    {
      totalDropped++;
      if (!_isDebug) 
        continue;
      Console.Clear();
      sandyCave.PrintWall();
      Thread.Sleep(100);
    }
    sandyCave.PrintWall();
    return totalDropped;
  }

  private static long DoPart1(IReadOnlyList<string> lines)
  {
    var sandyCave = new SandyCave(lines, 500, 0);
    var totalDropped = 0;
    while (sandyCave.DropSandUnit())
    {
      totalDropped++;
    }
    sandyCave.PrintWall();
    return totalDropped;
  }

  
}