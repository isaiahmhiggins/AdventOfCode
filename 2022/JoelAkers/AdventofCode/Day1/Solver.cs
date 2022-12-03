using System.Globalization;

namespace AdventofCode.Day1;

internal class Solver
{
  public int Solve(string filePath)
  {
    var file = File.ReadAllLines(filePath);
    var maxCalories = 0;
    var caloriesPerElf = new List<int>();
    var i = 0;
    while (i < file.Length)
    {
      var currentElfCalories = 0;
      while (i < file.Length && file[i].Length != 0)
      {
        currentElfCalories += int.Parse(file[i]);
        i++;
      }

      caloriesPerElf.Add(currentElfCalories);

      i++;
    }
    caloriesPerElf.Sort();
    return caloriesPerElf.TakeLast(3).Sum();
  }
}