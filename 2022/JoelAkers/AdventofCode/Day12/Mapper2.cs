using System.Numerics;
using System.Reflection.Metadata.Ecma335;

namespace AdventofCode.Day12;

public class Mapper2
{
  private Coord _startingPosition;
  private Coord _endPosition;
  private readonly List<List<Coord>> _startingMap = new();
  private readonly Queue<PathPoint> _pointsToCheck = new();
  public Mapper2(IReadOnlyList<string> fileLines)
  {
    ImportMap(fileLines);
  }

  public PathPoint FindPath()
  {
    var startingPoint = new PathPoint(_startingPosition);
    _pointsToCheck.Enqueue(startingPoint);
    PathPoint? currentPoint = null;
    while (_pointsToCheck.Count > 0)
    {
      currentPoint = _pointsToCheck.Dequeue();
      var currentCoord = currentPoint.Coordinate;
      if (currentCoord.Height == 'a')
      {
        return currentPoint;
      }

      TryAddCoordinateToQueue(currentCoord.X - 1, currentCoord.Y, currentPoint);
      TryAddCoordinateToQueue(currentCoord.X + 1, currentCoord.Y, currentPoint);
      TryAddCoordinateToQueue(currentCoord.X, currentCoord.Y - 1, currentPoint);
      TryAddCoordinateToQueue(currentCoord.X, currentCoord.Y + 1, currentPoint);

    }

    return currentPoint;
  }

  private bool TryAddCoordinateToQueue(int x, int y, PathPoint currentPoint)
  {
    if (x < 0 || y < 0 || x >= _startingMap[0].Count || y >= _startingMap.Count)
      return false;

    var currentCoord = currentPoint.Coordinate;
    var coordToAdd = _startingMap[y][x];
    if (coordToAdd.Visited || currentCoord.Height - coordToAdd.Height > 1) 
      return false;

    coordToAdd.Visited = true;
    var rightPointToAdd = new PathPoint(coordToAdd)
    {
      Children = new List<PathPoint>(),
      Parent = currentPoint
    };
    _pointsToCheck.Enqueue(rightPointToAdd);
    return true;
  }

  private void ImportMap(IReadOnlyList<string> fileLines)
  {
    for (var i = 0; i < fileLines.Count; i++)
    {
      var row = fileLines[i];
      var nextRow = new List<Coord>();
      for (var j = 0; j < row.Length; j++)
      {
        var item = row[j];
        switch (item)
        {
          case 'E':
            _startingPosition = new Coord { Height = 'z', Visited = false, X = j, Y = i };
            nextRow.Add(_startingPosition);
            break;
          default:
            nextRow.Add(new Coord { Height = item, Visited = false, X = j, Y = i });
            break;
        }
      }
      _startingMap.Add(nextRow);
    }
  }

  public void PrintMap(PathPoint finalPoint)
  {
    var map = new List<List<char>>();
    foreach (var row in _startingMap)
    {
      var line = new List<char>();
      foreach (var coord in row)
      {
        if (coord == _endPosition)
        {
          line.Add('E');
        }
        else if (coord.Visited)
        {
          line.Add('#');
        }
        else
        {
          line.Add('.');
        }
      }
      map.Add(line);
    }
    var lastPoint = finalPoint;
    var currentPoint = finalPoint.Parent;
    while (currentPoint.Coordinate != _startingPosition)
    {
      if (currentPoint.Coordinate == _startingPosition)
      {
        map[currentPoint.Coordinate.Y][currentPoint.Coordinate.X] = 'E';
      }
      else if (lastPoint.Coordinate.X < currentPoint.Coordinate.X)
      {
        map[currentPoint.Coordinate.Y][currentPoint.Coordinate.X] = '>';
      }
      else if (lastPoint.Coordinate.X > currentPoint.Coordinate.X)
      {
        map[currentPoint.Coordinate.Y][currentPoint.Coordinate.X] = '<';
      }
      else if (lastPoint.Coordinate.Y < currentPoint.Coordinate.Y)
      {
        map[currentPoint.Coordinate.Y][currentPoint.Coordinate.X] = 'V';
      }
      else if (lastPoint.Coordinate.Y > currentPoint.Coordinate.Y)
      {
        map[currentPoint.Coordinate.Y][currentPoint.Coordinate.X] = '^';
      }

      lastPoint = currentPoint;
      currentPoint = currentPoint.Parent;
    }

    Console.WriteLine("=================================");
    foreach (var line in map)
    {
      Console.WriteLine(new string(line.ToArray()));
    }
    Console.WriteLine("=================================");
  }
}