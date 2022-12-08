namespace AdventofCode.Day7;

public class CommandLineParser
{
  public CommandLineParser(string[] fileLines)
  {
    this._fileLines = fileLines;
    MainDirectory = new Directory("/");
    CurrentDirectory = MainDirectory;
  }

  public Directory? MainDirectory { get; set; }
  private Directory? CurrentDirectory { get; set; }

  private readonly string[] _fileLines;
  private int _currentIndex = 0;

  public void ParseLines()
  {
    while (_currentIndex < _fileLines.Length)
    {
      var splitLine = _fileLines[_currentIndex].Split();
      if (splitLine[0] == "$")
      {
        _currentIndex++;
        switch (splitLine[1])
        {
          case "cd":
            HandleChangeDirectory(splitLine[2]);
            break;
          case "ls":
            HandleListContents();
            break;
        }
      }
      else
      {
        throw new Exception($"Unexpected line: {splitLine}");
      }
    }
  }

  private void HandleListContents()
  {
    var isEndOfList = false;
    while (_currentIndex < _fileLines.Length && !isEndOfList)
    {
      var splitLine = _fileLines[_currentIndex].Split();
      
      switch (splitLine[0])
      {
        case "$":
          isEndOfList = true;
          break;
        case "dir":
          CurrentDirectory?.AddSubDirectory(splitLine[1]);
          _currentIndex++;
          break;
        default:
          CurrentDirectory?.AddFile(splitLine[1], splitLine[0]);
          _currentIndex++;
          break;
      }

    }
  }

  private void HandleChangeDirectory(string name) =>
    CurrentDirectory = name switch
    {
      "/" => MainDirectory,
      ".." => CurrentDirectory?.ParentDirectory,
      _ => CurrentDirectory?.SubDirectories.First(directory => directory?.Name == name)
    };
}