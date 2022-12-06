using MoreLinq;
namespace AdventofCode.Day6;

public class Solver
{
  public void Solve(string filePath, int partNumber)
  {
    var fileLines = File.ReadAllLines(filePath);
    var result = partNumber switch
    {
      2 => DoPart2(fileLines),
      1 => DoPart1(fileLines)
    };
    Console.Write($"Result is: {result}");
  }

  private int DoPart2(string[] lines)
  {
    var firstLine = lines[0];
    var i = 0;
    var subPart = new Queue<char>();
    while (i < firstLine.Length - 13)
    {
      var nextLetter = firstLine[i];
      if (subPart.Contains(nextLetter))
      {
        while (subPart.Dequeue() != nextLetter) { };
        subPart.Enqueue(nextLetter);
      }
      else if (subPart.Count < 13)
      {
        subPart.Enqueue(nextLetter);
      }
      else
      {
        return i + 1;
      }

      i++;
    }
    return 0;
  }

  private int DoPart1(string[] lines)
  {
    var firstLine = lines[0];
    var i = 0;
    var subPart = new Queue<char>();
    while (i < firstLine.Length - 3)
    {
      var nextLetter = firstLine[i];
      if (subPart.Contains(nextLetter))
      {
        while(subPart.Dequeue() != nextLetter) {};
        subPart.Enqueue(nextLetter);
      }
      else if (subPart.Count < 3)
      {
        subPart.Enqueue(nextLetter);
      }
      else
      {
        return i + 1;
      }

      i++;
    }
    return 0;
  }
}