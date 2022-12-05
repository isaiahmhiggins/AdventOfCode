namespace AdventofCode.Day5;

public class Mover
{
  private int moveFrom;
  private int moveTo;
  private int numCrates;

  public Mover(int moveFrom, int moveTo, int numCrates)
  {
    this.moveFrom = moveFrom;
    this.moveTo = moveTo;
    this.numCrates = numCrates;
  }

  public List<List<char>> Move1(List<List<char>> currentBoard)
  {
    var cratesToMove = currentBoard[moveFrom - 1].TakeLast(numCrates).ToList();
    currentBoard[moveFrom - 1].RemoveRange(currentBoard[moveFrom - 1].Count - numCrates, numCrates);
    cratesToMove.Reverse();
    currentBoard[moveTo - 1].AddRange(cratesToMove);
    return currentBoard;
  }

  public List<List<char>> Move2(List<List<char>> currentBoard)
  {
    var cratesToMove = currentBoard[moveFrom - 1].TakeLast(numCrates).ToList();
    currentBoard[moveFrom - 1].RemoveRange(currentBoard[moveFrom - 1].Count - numCrates, numCrates);
    currentBoard[moveTo - 1].AddRange(cratesToMove);
    return currentBoard;
  }
}