namespace AdventofCode.Day12;

public class PathPoint
{
  public PathPoint(Coord coordinate)
  {
    Coordinate = coordinate;
  }
  public List<PathPoint> Children = new();
  public PathPoint? Parent;
  public Coord Coordinate;

}