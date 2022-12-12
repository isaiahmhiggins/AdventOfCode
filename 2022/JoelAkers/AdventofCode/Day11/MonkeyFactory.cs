using System.Numerics;

namespace AdventofCode.Day11;

public class MonkeyFactory
{
  public List<int> Divisors = new() {3};
  public Monkey Create(string startingItems, string operation, string test, string ifTrue, string ifFalse, bool withRelief = true)
  {
    // Starting Items: Assuming form " ##, #, ###"
    var items = startingItems
      .Split(',')
      .Select(part => part.Trim())
      .Select(int.Parse)
      .ToList();

    var operationComponents = operation.Trim().Split(' ').Skip(3).ToList();
    var isNumber = int.TryParse(operationComponents[1], out var constantOperatingValue);
    var operatingSign = operationComponents[0].First();

    long OperationFunc(long input)
    {
      switch (operatingSign)
      {
        case '+':
          if (isNumber) return input + constantOperatingValue;
          return input + input;
        case '-':
          if (isNumber) return input - constantOperatingValue;
          return 0;
        case '*':
          if (isNumber) return input * constantOperatingValue;
          return input * input;
        default:
          throw new ArgumentException();
      }
    }

    var ifTrueMonkeyToCatch = ifTrue.Trim().Split(' ').Skip(3).Select(int.Parse).First();
    var ifFalseMonkeyToCatch = ifFalse.Trim().Split(' ').Skip(3).Select(int.Parse).First();
    var divisor = test.Trim().Split(' ').Skip(2).Select(int.Parse).First();
    int TestFunc(long input)
    {
      return input % divisor == 0 ? ifTrueMonkeyToCatch : ifFalseMonkeyToCatch;
    }

    Divisors.Add(divisor);
    Console.WriteLine($"Items: {string.Join(',', items)}");
    return new Monkey(items, OperationFunc, TestFunc, withRelief);
  }
}