namespace AdventofCode.Day2;

public class Solver
{
  public int Solve(string filePath)
  {
    var fileLines = File.ReadAllLines(filePath);
    var totalPoints = 0;
    var i = 0;
    while (i < fileLines.Length)
    {
      var line = fileLines[i];
      var splitLine = line.Split(' ');
      var opponent = splitLine[0][0];
      var winLose = splitLine[1][0];
      totalPoints += InterpretLinePart2(opponent, winLose);
      i++;
    }
    return totalPoints;
  }

  private static int InterpretLinePart2(char opponent, char winLose)
  {
    var scoreForWinLose = winLose switch
    {
      'X' => 0,
      'Y' => 3,
      'Z' => 6
    };
    var scoreForShape = ScoreFromShapePart2(opponent, winLose);
    return scoreForShape + scoreForWinLose;
  }

  private static int ScoreFromShapePart2(char opponent, char winLose)
  {

    return opponent switch
    {
      'A' => winLose switch
      {
        'X' => 3,
        'Y' => 1,
        'Z' => 2,
        _ => throw new ArgumentOutOfRangeException(nameof(winLose), winLose, null)
      },
      'B' => winLose switch
      {
        'X' => 1,
        'Y' => 2,
        'Z' => 3,
        _ => throw new ArgumentOutOfRangeException(nameof(winLose), winLose, null)
      },
      'C' => winLose switch
      {
        'X' => 2,
        'Y' => 3,
        'Z' => 1,
        _ => throw new ArgumentOutOfRangeException(nameof(winLose), winLose, null)
      },
      _ => throw new ArgumentOutOfRangeException(nameof(opponent), opponent, null)
    };
  }

  private static int InterpretLinePart1(char opponent, char me)
  {
    return ScoreFromShapePart1(me) + ScoreFromWinLosePart1(opponent, me);
  }

  private static int ScoreFromWinLosePart1(char opponent, char me)
  {
    return opponent switch
    {
      'A' => me switch
      {
        'X' => 3,
        'Y' => 6,
        'Z' => 0,
        _ => throw new ArgumentOutOfRangeException(nameof(me), me, null)
      },
      'B' => me switch
      {
        'X' => 0,
        'Y' => 3,
        'Z' => 6,
        _ => throw new ArgumentOutOfRangeException(nameof(me), me, null)
      },
      'C' => me switch
      {
        'X' => 6,
        'Y' => 0,
        'Z' => 3,
        _ => throw new ArgumentOutOfRangeException(nameof(me), me, null)
      },
      _ => throw new ArgumentOutOfRangeException(nameof(opponent), opponent, null)
    };
  }

  private static int ScoreFromShapePart1(char shape)
  {
    return shape switch
    {
      'X' => 1,
      'Y' => 2,
      'Z' => 3,
      _ => throw new Exception($"not expected value: {shape}")
    };
  }
}