def getMax(root):
    if root == None:
        return -1
    
    maxNode = root.data
    
    for child in root.children:
        maxNode = max(getMax(child), maxNode)
    
    return maxNode
