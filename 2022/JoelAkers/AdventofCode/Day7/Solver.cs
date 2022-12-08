namespace AdventofCode.Day7;

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
    var commandLineParser = new CommandLineParser(lines);
    commandLineParser.ParseLines();
    var neededSpace = 30000000;
    var currentlyUsedSpace = commandLineParser.MainDirectory.GetSize();
    var minimumMoreNeeded = currentlyUsedSpace - neededSpace;
    return GetDirectoryWithSmallestSizeMoreThan(minimumMoreNeeded, commandLineParser.MainDirectory);
  }

  private int DoPart1(string[] lines)
  {
    var commandLineParser = new CommandLineParser(lines);
    commandLineParser.ParseLines();
    return GetSumOfSubsLessThan(100000, commandLineParser.MainDirectory);
  }

  private int GetDirectoryWithSmallestSizeMoreThan(int minimum, Directory directory)
  {
    var currentDirectorySize = directory.GetSize();

    var subDirectoryMinimums = directory
      .SubDirectories
      .Select(subDir => GetDirectoryWithSmallestSizeMoreThan(minimum, subDir))
      .ToList();

    subDirectoryMinimums.Add(currentDirectorySize);

    var minimumsThatMeetRequirment = subDirectoryMinimums
      .Where(size => size > minimum)
      .ToList();
    return minimumsThatMeetRequirment.Count > 0 
      ? minimumsThatMeetRequirment.Min() 
      : int.MaxValue;

  }

  private int GetSumOfSubsLessThan(int maximum, Directory? directory)
  {
    if (directory.SubDirectories.Count == 0)
    {
      return directory.GetSize() <= maximum ? directory.GetSize() : 0;
    }

    var total = directory.GetSize() <= maximum ? directory.GetSize() : 0;
    total += directory.SubDirectories.Select(subDir => GetSumOfSubsLessThan(maximum, subDir)).Sum();
    return total;
  }
}