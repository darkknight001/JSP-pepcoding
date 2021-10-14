def areSimilar(root1, root2):
    if len(root1.children) != len(root2.children):
        return False
    
    isSimilar = True
    for i in range(len(root1.children)):
        if not areSimilar(root1.children[i], root2.children[i]):
            isSimilar = False
            break
    return isSimilar