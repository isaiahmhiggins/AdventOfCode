namespace AdventofCode.Day10;

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
    new Artist(lines).Draw();
    return 0;
  }

  private static int DoPart1(IEnumerable<string> lines)
  {
    var cyclesToCheck = new List<int> { 20, 60, 100, 140, 180, 220 };
    var valuePerCycle = new List<int>();
    var currentCycle = 0;
    var registerValue = 1;
    foreach (var line in lines)
    {
      var splitLine = line.Split(' ');
      switch (splitLine[0])
      {
        case "noop":
          currentCycle++;
          if (cyclesToCheck.Contains(currentCycle))
          {
            valuePerCycle.Add(currentCycle * registerValue);
          }
          break;
        case "addx":
          var value = int.Parse(splitLine[1]);
          for (var i = 0; i < 2; i++)
          {
            currentCycle++;
            if (cyclesToCheck.Contains(currentCycle))
            {
              valuePerCycle.Add(currentCycle * registerValue);
            }
          }
          registerValue += value;
          break;
      }
    }
    return valuePerCycle.Sum();
  }
}