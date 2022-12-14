using System.Text.Json.Nodes;

namespace AdventofCode.Day13;

public class JsonArrayComparator : Comparer<string>
{
  public static bool IsLeftLessThanOrEqualTo(string left, string right)
  {
    var leftJson = JsonNode.Parse(left);
    var rightJson = JsonNode.Parse(right);

    return Compare(leftJson, rightJson) != Equivalence.LeftIsLarger;
  }

  private static Equivalence Compare(JsonNode left, JsonNode right)
  {
    var leftIsArray = left is JsonArray;
    var rightIsArray = right is JsonArray;

    // One is digit and the other is array
    JsonArray? leftArray;
    JsonArray? rightArray;

    if (leftIsArray != rightIsArray)
    {
      leftArray = leftIsArray
        ? left as JsonArray
        : new JsonArray(left.GetValue<int>());
      rightArray = rightIsArray
        ? right as JsonArray
        : new JsonArray(right.GetValue<int>());

      return Compare(leftArray, rightArray);
    }

    // both are digit
    if (!leftIsArray && !rightIsArray)
    {
      var leftValue = left.GetValue<int>();
      var rightValue = right.GetValue<int>();
      if (leftValue == rightValue)
        return Equivalence.LeftIsEqual;
      if (leftValue < rightValue)
        return Equivalence.LeftIsSmaller;
      if (leftValue > rightValue)
        return Equivalence.LeftIsLarger;
    }

    //both are arrays
    leftArray = left as JsonArray;
    rightArray = right as JsonArray;
    var minLength = Math.Min(leftArray.Count, rightArray.Count);


    for (var i = 0; i < minLength; i++)
    {
      var equivalence = Compare(leftArray[i], rightArray[i]);
      if (equivalence != Equivalence.LeftIsEqual)
        return equivalence;
    }

    // check for count difference
    if (leftArray.Count < rightArray.Count)
    {
      return Equivalence.LeftIsSmaller;
    }
    return leftArray.Count > rightArray.Count
      ? Equivalence.LeftIsLarger
      : Equivalence.LeftIsEqual;
  }

  public override int Compare(string x, string y)
  {
    var leftJson = JsonNode.Parse(x);
    var rightJson = JsonNode.Parse(y);
    return Compare(leftJson, rightJson) switch
    {
      Equivalence.LeftIsEqual => 0,
      Equivalence.LeftIsSmaller => -1,
      Equivalence.LeftIsLarger => 1,
      _ => throw new ArgumentOutOfRangeException()
    };
  }
}