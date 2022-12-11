namespace AdventofCode.Day8;

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
    var forrest = new Forrest(lines);
    var totalVisibleTrees = forrest.GetMaximumScenicScore();
    return totalVisibleTrees;
  }

  private static int DoPart1(IEnumerable<string> lines)
  {
    var forrest = new Forrest(lines);
    var totalVisibleTrees = forrest.GetAllVisibleTrees().Count;
    forrest.PrintForrestVisibility();
    return totalVisibleTrees;
  }
}