namespace AdventofCode.Day4;

public class Solver
{
  public int Solve(string filePath, int partNumber)
  {
    var fileLines = File.ReadAllLines(filePath);
    return partNumber switch
    {
      2 => ByLinePart2(fileLines),
      1 => ByLinePart1(fileLines)
    };
  }

  private static int InterpretLinePart2(string line)
  {
    var elfPairs = line.Split(',');
    var elf1Pair = elfPairs[0].Split('-').Select(int.Parse).ToArray();
    var elf2Pair = elfPairs[1].Split('-').Select(int.Parse).ToArray();
    var list1 = Enumerable.Range(elf1Pair[0], elf1Pair[1] - elf1Pair[0] + 1).ToList();
    var list2 = Enumerable.Range(elf2Pair[0], elf2Pair[1] - elf2Pair[0] + 1).ToList();
    var overlaps = list1.Any(item => list2.Contains(item));
    return overlaps ? 1 : 0;
  }

  private static int ByLinePart2(string[] lines)
  {
    var totalPoints = 0;
    var i = 0;
    while (i < lines.Length)
    {
      var line = lines[i];
      totalPoints += InterpretLinePart2(line);
      i++;
    }
    return totalPoints;
  }

  private static int ByLinePart1(string[] lines)
  {
    var totalPoints = 0;
    var i = 0;
    while (i < lines.Length)
    {
      var line = lines[i];
      totalPoints += InterpretLinePart1(line);
      i++;
    }
    return totalPoints;

  }

  private static int InterpretLinePart1(string line)
  {
    var elfPairs = line.Split(',');
    var elf1Pair = elfPairs[0].Split('-').Select(int.Parse).ToArray();
    var elf2Pair = elfPairs[1].Split('-').Select(int.Parse).ToArray();
    if ((elf1Pair[0] <= elf2Pair[0] && elf1Pair[1] >= elf2Pair[1])
        || (elf1Pair[0] >= elf2Pair[0] && elf1Pair[1] <= elf2Pair[1]))
      return 1;
    return 0;
  }
}