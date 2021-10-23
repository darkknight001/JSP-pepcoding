predecessor = None
successor = None
state = -1
# Void function: updates pred ans successor of a given node directly into global variable
def predecessorAndSuccessor(root, data):
    global predecessor
    global successor
    global state
    
    if state==-1:
        if root.data==data:
            state+=1
        else:
            predecessor = root
    
    else:
        successor = root
        state+=1
        return
    
    for child in root.children:
        if successor is None:
            predecessorAndSuccessor(child, data)