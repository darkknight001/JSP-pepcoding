def areMirror(root1, root2):
    if len(root1.children) != len(root2.children):
        return False
    
    isMirror = True
    for i in range(len(root1.children)):
        if not areMirror(root1.children[i], root2.children[len(root2.children)-1-i]):
            isMirror = False
            break
    return isMirror

def isSymettric(root):
    return areMirror(root, root)
    