using System.Numerics;

namespace AdventofCode.Day11;

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
    var monkeyFactory = new MonkeyFactory();
    var monkeys = new List<Monkey>();
    var i = 0;
    while (i < lines.Count)
    {
      var nextLine = lines[i];
      if (nextLine == "")
      {
        i++;
        continue;
      }
      Console.WriteLine($"Setting up {nextLine}");
      i++;
      var startingValues = lines[i].Split(':')[1];
      i++;
      var operation = lines[i].Split(':')[1];
      i++;
      var test = lines[i].Split(':')[1];
      i++;
      var ifTrue = lines[i].Split(':')[1];
      i++;
      var ifFalse = lines[i].Split(':')[1];
      i++;
      monkeys.Add(monkeyFactory.Create(startingValues, operation, test, ifTrue, ifFalse, false));
    }

    foreach (var monkey in monkeys)
    {
      monkey.SetDivisors(monkeyFactory.Divisors);
    }
    const int turns = 10000;
    for (var j = 0; j < turns; j++)
    {
      foreach (var monkey in monkeys)
      {
        monkey.TakeTurn(monkeys);
      }
    }
    SeeMonkeysState(monkeys);

    var totalInspections = monkeys.Select(monkey => monkey.TotalInspections).ToList();
    var max = totalInspections.Max();
    totalInspections.Remove(max);
    var secondMax = totalInspections.Max();
    return max * secondMax;
  }

  private static long DoPart1(IReadOnlyList<string> lines)
  {
    var monkeyFactory = new MonkeyFactory();
    var monkeys = new List<Monkey>();
    var i = 0;
    while (i < lines.Count)
    {
      var nextLine = lines[i];
      if (nextLine == "")
      {
        i++;
        continue;
      }
      Console.WriteLine($"Setting up {nextLine}");
      i++;
      var startingValues = lines[i].Split(':')[1];
      i++;
      var operation = lines[i].Split(':')[1];
      i++;
      var test = lines[i].Split(':')[1];
      i++;
      var ifTrue = lines[i].Split(':')[1];
      i++;
      var ifFalse = lines[i].Split(':')[1];
      i++;
      monkeys.Add(monkeyFactory.Create(startingValues, operation, test, ifTrue, ifFalse));
    }


    foreach (var monkey in monkeys)
    {
      monkey.SetDivisors(monkeyFactory.Divisors);
    }
    const int turns = 20;
    for (var j = 0; j < turns; j++)
    {
      Console.WriteLine();
      Console.WriteLine($"Round {j + 1}");
      foreach (var monkey in monkeys)
      {
        Console.WriteLine();
        monkey.TakeTurn(monkeys);
        SeeMonkeysState(monkeys);
      }
    }

    var totalInspections = monkeys.Select(monkey => monkey.TotalInspections).ToList();
    var max = totalInspections.Max();
    totalInspections.Remove(max);
    var secondMax = totalInspections.Max();

    return max * secondMax;
  }

  private static void SeeMonkeysState(IReadOnlyList<Monkey> monkeys)
  {
    for (var i = 0; i < monkeys.Count; i++) {
      var items = string.Join(',', monkeys[i].GetCurrentHoldings());
      Console.WriteLine($"Monkey {i} has {items}");
      Console.WriteLine($"Monkey {i} has inspected {monkeys[i].TotalInspections} times");
    }
  }
}