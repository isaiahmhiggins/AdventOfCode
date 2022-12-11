namespace AdventofCode.Day7;

public class Directory
{
  public Directory(string name)
  {
    Name = name;
  }

  public string Name { get; set; }
  public Directory? ParentDirectory { get; set; }
  public List<Directory> SubDirectories = new();
  public List<Files> ContainedFiles = new();
  private int Size { get; set; } = -1;
  public void AddSubDirectory(string name)
  {
    SubDirectories.Add(new Directory(name)
    {
      ParentDirectory = this
    });
  }

  public void AddFile(string name, string size)
  {
    ContainedFiles.Add(new Files(name, size));
  }

  public int GetSize()
  {
    var total = ContainedFiles.Select(file => file.Size).Sum();
    total += SubDirectories.Select(directory => directory.GetSize()).Sum();
    Size = total;
    return total;
  }
}

public class Files
{
  public Files(string name, string size)
  {
    Name = name;
    Size = int.Parse(size);
  }
  public string Name { get; set; }
  public int Size { get; set; }
}