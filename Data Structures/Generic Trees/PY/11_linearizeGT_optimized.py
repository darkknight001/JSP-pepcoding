# Time complexity: 0{N}


def linearize2(root):
    if len(root.children)==0:
        return root
        
    tree1Ltail = linearize2(root.children[-1])
    
    while(len(root.children)>1):
        tree1L = root.children.pop(-1)
        tree2L = root.children[-1]
        
        tree2LTail = linearize2(root.children[-1])
        tree2LTail.children.append(tree1L)
    return tree1Ltail