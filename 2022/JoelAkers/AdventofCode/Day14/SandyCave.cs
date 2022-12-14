using System.Numerics;

namespace AdventofCode.Day14;

public class SandyCave
{
  public List<List<char>> CaveWalls { get; } = new();
  private readonly Vector2 _topLeftCoordinate;
  public Vector2 SandSource { get; }
  public SandyCave(IReadOnlyList<string> fileLines, int sourceX, int sourceY, bool withVoid = true)
  {
    SandSource = new Vector2(sourceX, sourceY);
     var wallsToDraw = fileLines
       .Select(ParseLine)
       .ToList();

     var minimumY = (int)Math.Min(wallsToDraw.Min(row => row.Min(item => item.Y)), 0);
     var maximumY = (int)wallsToDraw.Max(row => row.Max(item => item.Y));
     var minimumX = (int)wallsToDraw.Min(row => row.Min(item => item.X));
     var maximumX = (int)wallsToDraw.Max(row => row.Max(item => item.X));

     if (!withVoid)
     {
        maximumY += 2;
        var totalDesiredWidth = maximumY - minimumY + 100;
        minimumX = Math.Min(minimumX, sourceX - totalDesiredWidth);
        maximumX = Math.Max(maximumX, sourceX + totalDesiredWidth);
     }

     _topLeftCoordinate = new Vector2(minimumX, minimumY);
     
     for (var i = minimumY; i <= maximumY; i++)
     {
       var nextRow = new List<char>();
       for (var j = minimumX; j <= maximumX; j++)
       {
         if (i == 0 && j == 500)
         {
           nextRow.Add('+');
         }
         else if (!withVoid && i == maximumY)
          {
            nextRow.Add('#');
            
          }
         else
         {
           nextRow.Add('.');
         }
       }
       CaveWalls.Add(nextRow);
     }
     PrintWall();

     foreach (var wall in wallsToDraw)
     {
       DrawWall(wall);
     }
     PrintWall();
  }

  public void PrintWall()
  {
    Console.WriteLine();
    foreach (var row in CaveWalls)
    {
      Console.WriteLine(new string(row.ToArray()));
    }
  }

  public bool DropSandUnit(int x = -1, int y = -1)
  {
    if (x == -1)
    {
      x = (int)SandSource.X;
    }
    if (y == -1)
    {
      y = (int)SandSource.Y;
    }

    //returns false if fell off
    var currentPosition = new Vector2(x -_topLeftCoordinate.X , y);
    while (true)
    {
      if (CaveWalls[(int)(SandSource.Y - _topLeftCoordinate.Y)][(int)(SandSource.X - _topLeftCoordinate.X)] == 'O')
      {
        return false;
      }
      if (currentPosition.Y + 1 >= CaveWalls.Count)
      {
        return false;
      }

      if (CaveWalls[(int)currentPosition.Y + 1][(int)currentPosition.X] == '.')
      {
        currentPosition.Y++;
        continue;
      }

      if (currentPosition.X == 0)
      {
        return false;
      }

      if (CaveWalls[(int)currentPosition.Y + 1][(int)currentPosition.X - 1] == '.')
      {
        currentPosition.Y++;
        currentPosition.X--;
        continue;
      }

      if (currentPosition.X == CaveWalls[0].Count - 1)
      {
        return false;
      }

      if (CaveWalls[(int)currentPosition.Y + 1][(int)currentPosition.X + 1] == '.')
      {
        currentPosition.Y++;
        currentPosition.X++;
        continue;
      }

      CaveWalls[(int)currentPosition.Y][(int)currentPosition.X] = 'O';

      return true;
    }
  }

  private void DrawWall(IReadOnlyList<Vector2> wallToDraw)
  {
    for (var wall = 0; wall < wallToDraw.Count - 1; wall++)
    { 
      var countY =  Math.Max(Math.Abs(wallToDraw[wall + 1].Y - wallToDraw[wall].Y) + 1, 1);
      var countX = Math.Max(Math.Abs(wallToDraw[wall + 1].X - wallToDraw[wall].X) + 1, 1);
      var startY = Math.Min(wallToDraw[wall].Y, wallToDraw[wall + 1].Y);
      var startX = Math.Min(wallToDraw[wall].X, wallToDraw[wall + 1].X);
      var rangeY = Enumerable.Range((int)startY, (int)countY).ToList();
      var rangeX = Enumerable.Range((int)startX, (int)countX).ToList();
      foreach (var y in rangeY)
      {
        foreach (var x in rangeX)
        {

          CaveWalls[y - (int)_topLeftCoordinate.Y][x - (int)_topLeftCoordinate.X] = '#';
        }
      }
    }
  }

  private static List<Vector2> ParseLine(string line)
  {
    return line
      .Split("->")
      .Select(item => item.Trim())
      .Select(coordinate =>
      {
        var numbers = coordinate
          .Split(',')
          .Select(int.Parse)
          .ToList();
        return new Vector2(numbers[0], numbers[1]);
      })
      .ToList();
  }
}