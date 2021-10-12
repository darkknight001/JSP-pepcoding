def levelOrderLineWiseZZ(root):
    # take a queue
    q = []
    # add root to queue
    q.append(root)
    st = []
    reverseOrder = False
    while(len(q)>0):
        cnt = len(q)
        for i in range(cnt):
            # remove node from queue
            temp = q.pop(0)
            
            if not reverseOrder:
                # print data of node
                print(temp.data, end=" ")
            else:
                st.append(temp.data)
                
            # add child of node to queue
            q.extend(temp.children)
        if reverseOrder:
            while(len(st)>0):
                print(st.pop(-1), end=" ")
            reverseOrder = False
        else:
            reverseOrder = True
        print()