using System.Numerics;

namespace AdventofCode.Day11;

public class Monkey
{
  private Func<long, long> Operation { get; }
  private readonly Queue<long> _itemsHeld = new();
  private Func<long, int> Test { get; }
  public long TotalInspections;
  private readonly bool _withRelief;
  public List<int> Divisors { get; set; }
  private int _minValueBeforeCut;
  private long _maxValueAllowed;
  public Monkey(List<int> startingItems, Func<long, long> operation, Func<long, int> test, bool withRelief = true)
  {
    foreach (var startingItem in startingItems)
    {
      _itemsHeld.Enqueue(startingItem);
    }
    Operation = operation;
    Test = test;
    _withRelief = withRelief;
  }

  public void SetDivisors(List<int> divisors)
  {
    Divisors = divisors;
  }

  public void TakeTurn(List<Monkey> monkeys)
  {
    while (_itemsHeld.Count > 0)
    {
      var nextItem = _itemsHeld.Dequeue();
      var checkItOut = Operation(nextItem);
      if (checkItOut < nextItem) throw new ArgumentOutOfRangeException();
      var monkeyGotBored = _withRelief ? DecreaseWorryLevel(checkItOut) : checkItOut;
      var monkeyToThrowTo = Test(monkeyGotBored);
      var cutValue = TryCutByDivisors(monkeyGotBored);
      monkeys[monkeyToThrowTo].CatchItem(cutValue);
      TotalInspections++;
    }
  }

  public void CatchItem(long value)
  {
    _itemsHeld.Enqueue(value);
  }

  public List<long> GetCurrentHoldings()
  {
    return _itemsHeld.ToList();
  }

  private long TryCutByDivisors(long value)
  {
    if (_minValueBeforeCut == 0)
    {
      _minValueBeforeCut = 1;
      Divisors.ForEach(item => _minValueBeforeCut *= item);
    }

    if (_maxValueAllowed == 0)
    {
      _maxValueAllowed = _minValueBeforeCut * 2;
    }
    
    if (value <= _maxValueAllowed) 
      return value;

    var remainder = value % _minValueBeforeCut;
    var result  = _minValueBeforeCut + remainder;

    return result;
  }

  private static long DecreaseWorryLevel(long input)
  {
    return (long)Math.Floor(input / 3.0);
  }
}