def height(root):
    if root is None:
        return -1

    if len(root.children) == 0:
      return 0

    treeHeight = -1
    for child in root.children:
      treeHeight  = max(treeHeight, height(child))
    treeHeight+=1

    return treeHeight
