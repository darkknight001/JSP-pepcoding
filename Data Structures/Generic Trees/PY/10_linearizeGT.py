# Time complexity: 0{N*N}


def getLastNode(root):
    while(len(root.children)!=0):
        root = root.children[0]
    return root

def linearize(root):
    for child in root.children:
        linearize(child)
    
    while(len(root.children)>1):
        tree1L = root.children.pop(-1)
        tree2L = root.children[-1]
        
        tree2LTail = getLastNode(tree2L)
        tree2LTail.children.append(tree1L)
    