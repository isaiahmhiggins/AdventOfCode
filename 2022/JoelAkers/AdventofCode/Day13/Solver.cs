using System.Linq.Expressions;
using System.Text.Json.Nodes;

namespace AdventofCode.Day13;

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
    var input = lines.Where(line => line.Length > 0).ToList();
    var dividends = new List<string> { "[[6]]" , "[[2]]"};
    input.AddRange(dividends);
    input.Sort(new JsonArrayComparator());
    foreach (var line in input)
    {
      Console.WriteLine(line);
    }
    var index1 = input.FindIndex(item => item == dividends[0]) + 1;
    var index2 = input.FindIndex(item => item == dividends[1]) + 1;
    return index1 * index2;
  }

  private static long DoPart1(IReadOnlyList<string> lines)
  {
    var sum = 0;
    var currentPair = 1;
    var i = 0;
    while (i < lines.Count)
    {
      Console.WriteLine();
      if (JsonArrayComparator.IsLeftLessThanOrEqualTo(lines[i], lines[i + 1]))
      {
        sum += currentPair;
        Console.WriteLine($"Pair {currentPair} is in the right order");
      }
      else
      {
        Console.WriteLine($"Pair {currentPair} is in the wrong order");
      }
      currentPair++;
      i += 3;
    }
    
    return sum;
  }

  
}