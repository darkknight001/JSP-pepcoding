def traversals(root):
    if root is None:
        return
    

    # pre-order
    print("Node Pre " + str(root.data))
    
    for child in root.children:
        # in-order
        print("Edge Pre " + str(root.data) + "--" + str(child.data))
        traversals(child)
        print("Edge Post " + str(root.data) + "--" + str(child.data))
    
    # post-order
    print("Node Post " + str(root.data))
    
