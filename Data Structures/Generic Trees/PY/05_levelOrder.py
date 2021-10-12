def levelOrder(root):
    # take a queue
    q = []
    
    # add root to queue
    q.append(root)
    
    while(len(q)>0):
        # remove node from queue
        temp = q.pop(0)
        # print data of node
        print(temp.data, end=" ")
        # add child of node to queue
        q.extend(temp.children)
        
    print(".")
