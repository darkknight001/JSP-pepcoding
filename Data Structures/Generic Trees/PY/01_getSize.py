class Node:
    def __init__(self):
        self.data = 0;
        self.children = []

n_items = int(input())
input_str = input()

def construct(input_str):
    st = []
    tree = list(map(int, input_str.split()))
    root = None;
    
    for i in range(len(tree)):
        
        if tree[i]==-1:
            st.pop()
        else:
            temp = Node()
            temp.data = tree[i]
            
            if(len(st)>0):
                st[-1].children.append(temp)
            else:
                root = temp
            
            st.append(temp)

    return root

def display(currNode):
    s = str(currNode.data) + " -> "
    
    for child in currNode.children:
        s += str(child.data) + ", "
    s += "."
    
    print(s)
    for child in currNode.children:
        display(child)

def size(node):
    if node == None:
        return 0
    
    counter = 1
    
    for child in node.children:
        counter+=1
    
    for child in node.children:
        counter+=size(child)-1
    
    return counter

root = construct(input_str)
print(size(root)+1)
display(root)
