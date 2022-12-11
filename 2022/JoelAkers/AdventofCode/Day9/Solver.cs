namespace AdventofCode.Day9;

public class Solver
{
  public void Solve(string filePath, int partNumber)
  {
    var fileLines = File.ReadAllLines(filePath);
    var result = partNumber switch
    {
      2 => DoPart2(fileLines),
      1 => DoPart1(fileLines),
      _ => throw new ArgumentOutOfRangeException(nameof(partNumber), partNumber, null)
    };
    Console.Write($"Result is: {result}");
  }

  private static int DoPart2(IEnumerable<string> lines)
  {
    return new Grid(lines, 2, 9, false).VisitedByLastKnot.Count;
  }

  private static int DoPart1(IEnumerable<string> lines)
  {
    return new Grid(lines, 2, 1, true).VisitedSpaces.Count;
  }
}