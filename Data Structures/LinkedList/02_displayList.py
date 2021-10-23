class Node:
    def __init__(self, val = -1, nextNode = None):
        self.data = val
        self.next = nextNode
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def addLast(self, val):
        newNode = Node(val)
        if self.size==0:
            self.head = self.tail = newNode
            self.size+=1
            
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
            self.size+=1
    
    def getSize(self):
        return self.size
        
    def display(self):
        temp = self.head
        
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Driver Code

def driver():
    queries = []
    ll = LinkedList()
    
    # Getting input to buffer array
    while True:
        line = input()
        if line and line!="quit":
            queries.append(line)
        else:
            break
    
    for q in queries:
        if "addLast" in q:
            val = int(q.split()[1])
            ll.addLast(val)
        elif "display" in q:
            ll.display()
        elif "size" in q:
            print(ll.getSize())
        
    

driver()
    
