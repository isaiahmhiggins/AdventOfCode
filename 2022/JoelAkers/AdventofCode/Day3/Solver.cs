namespace AdventofCode.Day3;

public class Solver
{
  public int Solve(string filePath, int partNumber)
  {
    var fileLines = File.ReadAllLines(filePath);
    return partNumber switch
    {
      2 => ByThreeLinesPart2(fileLines),
      1 => ByLinePart1(fileLines)
    };
  }

  private static int InterpretLinesPart2(string line1, string line2, string line3)
  {
    foreach (var ch in line1)
    {
      if (line2.Contains(ch) && line3.Contains(ch)) 
        return LetterToValue(ch);
    }

    throw new Exception("Matching letter not found in lines");
  }

  private static int ByThreeLinesPart2(string[] lines)
  {
    var totalPoints = 0;
    var i = 0;
    while (i < lines.Length)
    {
      totalPoints += InterpretLinesPart2(lines[i], lines[i+1], lines[i+2]);
      i += 3;
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
    return LetterToValue(FindDuplicateLetter(line));
  }

  private static char FindDuplicateLetter(string line)
  {
    var firstHalf = line.Take(line.Length / 2);
    var lastHalf = line.TakeLast(line.Length / 2);
    foreach (var ch in firstHalf)
    {
      if (lastHalf.Contains(ch)) 
        return ch;
    }

    throw new Exception("No letters were found to be duplicates");
  }

  private static int LetterToValue(char letter)
  {
    return letter switch
    {
      >= 'A' and <= 'Z' => letter - 'A' + 27,
      >= 'a' and <= 'z' => letter - 'a' + 1,
      _ => 0
    };
  }
}