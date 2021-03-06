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

def testList(linkedlist):
    temp = linkedlist.head
    
    while temp!=None:
        print(temp.data)
    
    print(linkedlist.size)
    
    if linkedlist.size > 0:
        print(linkedlist.tail.data)

# Driver Code

def driver():
    # Python bufferedInput implementation
    queries = []
    ll = LinkedList()
    
    # Getting input to buffer array
    while True:
        try:
            line = input()
        except EOFError:
            break
        queries.append(line)
    
    for q in queries:
        if q=="quit":
            break
        if "addLast" in q:
            val = int(q.split()[1])
            ll.addLast(val)
    
    testList(ll)
    
driver()
