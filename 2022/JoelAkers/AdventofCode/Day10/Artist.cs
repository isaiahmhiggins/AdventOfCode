namespace AdventofCode.Day10;

public class Artist
{
  private int _rowLength = 40;
  private string _drawnPixels = "";
  private int _currentRegisterValue = 1;
  private int _currentClockCycle;

  public Artist(IEnumerable<string> fileLines)
  {

    foreach (var line in fileLines)
    {
      var splitLine = line.Split(' ');
      switch (splitLine[0])
      {
        case "noop":
          SetNextPixel();
          _currentClockCycle++;
          break;
        case "addx":
          var value = int.Parse(splitLine[1]);
          for (var i = 0; i < 2; i++)
          {
            SetNextPixel();
            _currentClockCycle++;
          }
          _currentRegisterValue += value;
          break;
      }
    }
  }

  private void SetNextPixel()
  {
    if (_currentClockCycle % _rowLength == 0)
    {
      _drawnPixels += '\n';
    }
    var horizontalPos = _currentClockCycle % _rowLength;
    if (horizontalPos >= _currentRegisterValue - 1 && horizontalPos <= _currentRegisterValue + 1)
    {
      _drawnPixels += '#';
    }
    else
    {
      _drawnPixels += '.';
    }

    Console.WriteLine(_drawnPixels);
    Console.WriteLine($"Reg: {_currentRegisterValue}; Cycle: {_currentClockCycle}");
  }

  public void Draw()
  {
    Console.Write(_drawnPixels);
  }
}