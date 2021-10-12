def levelOrderLineWise1(root):
    # take a queue
    pq = []
    # add root to queue
    pq.append(root)
    while(len(pq)>0):
        cq = []
        while(len(pq)>0):
            # remove node from queue
            temp = pq.pop(0)
            # print data of node
            print(temp.data, end=" ")
            # add child of node to queue
            cq.extend(temp.children)
            
        print()
        pq = cq

def levelOrderLineWise2(root):
    # take a queue
    q = []
    # add root to queue
    q.append(root)
    dummy = Node();
    dummy.data = -1
    q.append(dummy)
    
    while(len(q)>0):
        # remove node from queue
        temp = q.pop(0)
        if(temp.data!=-1):
            # print data of node
            print(temp.data, end=" ")
            # add child of node to queue
            q.extend(temp.children)
        
        else:
            print()
            if(len(q)>0):
                q.append(dummy)

def levelOrderLineWise3(root):
    # take a queue
    q = []
    # add root to queue
    q.append(root)
    
    while(len(q)>0):
        cnt = len(q)
        for i in range(cnt):
            # remove node from queue
            temp = q.pop(0)
            # print data of node
            print(temp.data, end=" ")
            # add child of node to queue
            q.extend(temp.children)
        print()
