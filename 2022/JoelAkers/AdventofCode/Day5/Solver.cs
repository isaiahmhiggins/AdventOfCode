using MoreLinq;
namespace AdventofCode.Day5;

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

  private List<List<char>> GetBasketLines(string[] fileLines)
  {
    var basketLines = fileLines.Where(line => line.Length > 0 && line.TrimStart()[0] == '[').ToList();
    var baskets = basketLines
      .Select(line => line
        .Skip(1)
        .TakeEvery(4)
        .ToList())
      .ToList();
    
    return Rotate90(baskets);
  }

  private List<List<char>> Rotate90(List<List<char>> table)
  {
    var nextTable = table.Last().Select(value => new List<char> {value}).ToList();
    for (var i = table.Count - 2; i >= 0; i--)
    {
      for (var j = 0; j < table[i].Count; j++)
      {
        if (char.IsLetter(table[i][j]))
        {
          nextTable[j].Add(table[i][j]);
        }
      }
    }
    Console.WriteLine(nextTable);
    return nextTable;
  }

  private List<Mover> GetMovers(string[] fileLines)
  {
    var moveLines = fileLines.Where(line => line.StartsWith("move")).ToList();
    return moveLines
      .Select(line =>
      {
        var numbers = line
          .Split(' ')
          .Select(item =>
          {
            var isInt = int.TryParse(item, out var value);
            return isInt ? value : -1;
          })
          .Where(value => value >= 0)
          .ToList();
        return new Mover(numCrates: numbers[0], moveFrom: numbers[1], moveTo: numbers[2]);
      })
      .ToList();

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

  private string DoPart2(string[] lines)
  {
    var i = 0;
    var baskets = GetBasketLines(lines);
    var movers = GetMovers(lines);
    movers.ForEach(mover => baskets = mover.Move2(baskets));

    var topCrates = baskets.Select(stack => stack.LastOrDefault()).ToArray();
    var result = new string(topCrates);
    return result;
  }

  private string DoPart1(string[] lines)
  {
    var i = 0;
    var baskets = GetBasketLines(lines);
    var movers = GetMovers(lines);
    movers.ForEach(mover => baskets = mover.Move1(baskets));

    var topCrates = baskets.Select(stack => stack.LastOrDefault()).ToArray();
    var result = new string(topCrates);
    return result;

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