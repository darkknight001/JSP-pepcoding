def removeLeaves(root):
    for i in range(len(root.children)-1, -1, -1):
        child = root.children[i]
        if len(child.children)==0:
            # print("Removing "+str(root.data)+"->"+str(child.data))
            root.children.remove(child)
            
    for child in root.children:
        removeLeaves(child)
    