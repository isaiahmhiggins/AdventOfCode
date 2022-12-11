using System.Numerics;

namespace AdventofCode.Day9;

public class Grid
{
  public readonly List<Vector2> VisitedSpaces = new();
  public readonly List<Vector2> VisitedByLastKnot = new();
  private Vector2 _headPosition;
  private List<Vector2> _tails = new();
  private readonly int _stretchDist;
  private readonly int _tailCount;
  private readonly bool _printSteps;

  public Grid(IEnumerable<string> fileLines, int stretchDist, int tailCount, bool printSteps)
  {
    _stretchDist = stretchDist;
    _tailCount = tailCount;
    _printSteps = printSteps;

    for (var i = 0; i < _tailCount; i++)
    {
      _tails.Add(new Vector2());
    }

    _headPosition = new Vector2();
    VisitedSpaces.Add(new Vector2());
    VisitedByLastKnot.Add(new Vector2());
    foreach (var line in fileLines)
    {
      var splitLine = line.Split(' ');
      var direction = splitLine[0].First();
      var spaces = int.Parse(splitLine[1]);
      MoveHead(direction, spaces);

    }
  }

  private void TailFollows()
  {
    var lead = _headPosition;
    for (var i = 0; i < _tails.Count; i++)
    {
      if (Vector2.Distance(lead, _tails[i]) < _stretchDist) 
        return;

      var direction = lead - _tails[i];
      if (Math.Abs(MathF.Abs(direction.X) - MathF.Abs(direction.Y)) < 0.01)
      {
        _tails[i] += direction / 2;
      }
      else if (MathF.Abs(direction.Y) >= _stretchDist)
      {
        _tails[i] = lead with { Y = _tails[i].Y + (int)(direction.Y/ MathF.Abs(direction.Y)) };
      }
      else
      {
        _tails[i] = lead with { X = _tails[i].X + (int)(direction.X / MathF.Abs(direction.X)) };
      }

      if (VisitedSpaces.All(space => space != _tails[i]))
      {
        VisitedSpaces.Add(_tails[i]);
      }

      if (i==_tailCount - 1 && VisitedByLastKnot.All(space => space != _tails[i]))
      {
        VisitedByLastKnot.Add(_tails[i]);
      }

      if (_printSteps)
      {
        PrintGrid();

      }

      lead = _tails[i];
    }

  }

  private void MoveHead(char direction, int spaces)
  {
    switch (direction)
    {
      case 'U':
        for (var i = 0; i < spaces; i++)
        {
          _headPosition.Y++;
          TailFollows();
        }
        break;
      case 'D':
        for (var i = 0; i < spaces; i++)
        {
          _headPosition.Y--;
          TailFollows();
        }
        break;
      case 'R':
        for (var i = 0; i < spaces; i++)
        {
          _headPosition.X++;
          TailFollows();
        }
        break;
      case 'L':
        for (var i = 0; i < spaces; i++)
        {
          _headPosition.X--;
          TailFollows();
        }
        break;
    }
  }

  public void PrintGrid()
  {
    var maxX = (int)VisitedSpaces.Select(space => space.X).Max();
    var minX = (int)VisitedSpaces.Select(space => space.X).Min();
    var maxY = (int)VisitedSpaces.Select(space => space.Y).Max();
    var minY = (int)VisitedSpaces.Select(space => space.Y).Min();

    Console.WriteLine("##################################");
    for (var i = maxY + _stretchDist; i > minY - _stretchDist - 1; i--)
    {
      var line = "";
      for (var j = minX - _stretchDist; j < maxX + _stretchDist + 1; j++)
      {
        if (_headPosition == new Vector2(j, i))
        {
          line += "H";
        }
        else if (_tails.Contains(new Vector2(j, i)))
        {
          var indexOfFirst = _tails.IndexOf(new Vector2(j, i)) + 1;
          line += indexOfFirst.ToString();
        }
        else if (i == 0 && j == 0)
        {
          line += "s";
        }
        else if(VisitedByLastKnot.Contains(new Vector2(j, i)))
        {
          line += "#";
        }
        else
        {
          line += ".";
        }
      }
      Console.WriteLine(line);
    }
    
  }

}