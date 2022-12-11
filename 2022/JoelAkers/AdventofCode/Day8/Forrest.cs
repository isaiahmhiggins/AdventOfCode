using System.Transactions;

namespace AdventofCode.Day8;

public class Forrest
{
  public Forrest(IEnumerable<string> fileLines)
  {
    ReadMap(fileLines);
  }

  private List<List<Tree>> Trees { get; } = new();

  private void ReadMap(IEnumerable<string> fileLines)
  {
    foreach (var line in fileLines)
    {
      var treeLine = line
        .Select(height => new Tree(height - '0'))
        .ToList();
      Trees.Add(treeLine);
    }
  }

  public List<Tree> GetAllVisibleTrees()
  {
    for (var i = 0; i < Trees.Count; i++)
    {
      for (var j = 0; j < Trees[i].Count; j++)
      {
        SetTreeVisibility(i, j);
      }
    }
    return Trees
      .SelectMany(treeLine => treeLine.Where(tree => tree.Visible))
      .ToList();
  }

  private void SetTreeVisibility(int i, int j)
  {
    if (i == 0 || j == 0 || i == Trees.Count - 1 || j == Trees[i].Count - 1)
    {
      Trees[i][j].Visible = true;
      return;
    }
    var treeHeight = Trees[i][j].Height;
    //From Left
    var maxHeightOnLeft = Trees[i]
      .Take(j)
      .Max(tree => tree.Height);
    var maxHeightOnRight = Trees[i].TakeLast(Trees[i].Count - j - 1)
      .Max(tree => tree.Height);
    var maxHeightOnTop = Trees
      .Select(treeLine => treeLine[j])
      .Take(i)
      .Max(tree => tree.Height);
    var maxHeightOnBottom = Trees
      .Select(treeLine => treeLine[j]).TakeLast(Trees.Count - i - 1)
      .Max(tree => tree.Height);
    Trees[i][j].Visible = maxHeightOnLeft < treeHeight
      || maxHeightOnBottom < treeHeight
      || maxHeightOnRight < treeHeight
      || maxHeightOnTop < treeHeight;
  }

  public void PrintForrestVisibility()
  {
    foreach (var row in Trees)
    {
      var line = new string(row.Select(tree => tree.Visible ? '1' : 'O').ToArray());
      Console.WriteLine(line);
    }
  }
  public void PrintForrestScenicScore()
  {
    foreach (var row in Trees)
    {
      var line = string.Join(' ', row.Select(tree => tree.ScenicScore).ToArray());
      Console.WriteLine(line);
    }
  }

  public int GetMaximumScenicScore()
  {
    SetScenicScores();
    PrintForrestScenicScore();
    return Trees
      .SelectMany(treeLine => treeLine.Select(tree => tree.ScenicScore).ToList())
      .Max();
  }
  private void SetScenicScores()
  {
    for (var i = 0; i < Trees.Count; i++)
    {
      for (var j = 0; j < Trees[i].Count; j++)
      {
        var treeHeight = Trees[i][j].Height;
        var treesOnRight = Trees[i].TakeLast(Trees[i].Count - j - 1).ToList();
        var scoreFromRight = GetScoreForLineOfSight(treesOnRight, treeHeight);

        var treesOnLeft = Trees[i].Take(j).ToList();
        treesOnLeft.Reverse();
        var scoreFromLeft = GetScoreForLineOfSight(treesOnLeft, treeHeight);

        var treesOnTop = Trees
          .Take(i)
          .Select(line => line[j])
          .ToList();
        treesOnTop.Reverse();
        var scoreFromTop = GetScoreForLineOfSight(treesOnTop, treeHeight);

        var treesOnBottom = Trees
          .TakeLast(Trees.Count - i - 1)
          .Select(line => line[j])
          .ToList();
        var scoreFromBottom = GetScoreForLineOfSight(treesOnBottom, treeHeight);
        Trees[i][j].ScenicScore = scoreFromBottom * scoreFromLeft * scoreFromRight * scoreFromTop;
      }
    }
  }

  //Assumes Starting Tree is at -1
  private int GetScoreForLineOfSight(List<Tree> treeLine, int currentTreeHeight)
  {
    var score = 0;
    foreach (var tree in treeLine)
    {
      if (tree.Height >= currentTreeHeight)
      {
        score++;
        break;
      }

      score++;
    }
    return score;
  }
}

public class Tree
{
  public Tree(int height)
  {
    Height = height;
  }
  public bool Visible { get; set; }
  public int Height { get; set; }
  public int ScenicScore { get; set; }
}