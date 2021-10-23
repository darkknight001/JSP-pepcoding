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
    
    def removeFirst(self):
        if self.size==0:
            print("List is empty")
        else:
            self.head = self.head.next
            self.size-=1
    
    def getFirst(self):
        if self.size==0:
            print("List is empty")
            return -1
        else:
            return self.head.data

    def getLast(self):
        if self.size==0:
            print("List is empty")
            return -1
        else:
            return self.tail.data   
    
    def getAt(self, idx):
        if self.size==0:
            print("List is empty")
            return -1
        elif idx>self.size-1:
            print("Invalid arguments")
            return -1
        else:
            temp = self.head
            for i in range(idx):
                temp = temp.next
            return temp.data
    
    def addFirst(self, val):
        newNode = Node(val)
        if self.size==0:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
        self.size+=1
        
    def removeLast(self):
        if self.size==0:
            print("List is empty")
        elif self.size == 1:
            self.head = self.tail = None
            size=0
        else:
            temp = self.head
            for i in range(self.size-2):
                temp = temp.next
            temp.next = None
            self.tail = temp
            self.size-=1
    
    def addAt(self, val, idx):
        if idx<0 or idx> self.size:
            print("Invalid arguments")
            return
        elif idx==0 or self.size==0:
            self.addFirst(val)
        elif idx==self.size :
            self.addLast(val)
        else:
            newNode = Node(val)
            temp = self.head
            for i in range(idx-1):
                temp = temp.next
                
            newNode.next =temp.next
            temp.next = newNode
            self.size+=1
            
    def removeAt(self, idx):
        if idx<0 or idx >= self.size:
            print("Invalid arguments")
            return
        elif idx==0:
            self.removeFirst()
        elif idx==self.size-1:
            self.removeLast()
        else:
            temp = self.head
            for i in range(idx-1):
                temp = temp.next
                
            temp.next = temp.next.next
            self.size-=1
    
    def getNodeAt(self, idx):
        temp = self.head
        for i in range(idx):
            temp = temp.next
        return temp
    
    def reverseDI(self):
        l = 0
        r = self.size-1
        
        while(l<r):
            leftNode = self.getNodeAt(l)
            rightNode = self.getNodeAt(r)
            
            # temp = leftNode.data
            # leftNode.data = rightNode.data
            # rightNode.data = temp
            leftNode.data, rightNode.data = rightNode.data, leftNode.data
            l+=1
            r-=1
    
    def reversePI(self):
        if self.head == None or self.head.next == None:
            return
        
        prev = None
        curr = self.head
        ahead = curr.next
        
        while(curr!=None):
            curr.next = prev
            prev = curr
            curr = ahead
            
            if ahead!=None:
                ahead = ahead.next
        
        self.tail = self.head
        self.head = prev
    
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
        elif "addFirst" in q:
            val = int(q.split()[1])
            ll.addFirst(val)
        elif "addAt" in q:
            idx = int(q.split()[1])
            val = int(q.split()[2])
            ll.addAt(val, idx)
            
        elif "display" in q:
            ll.display()
        elif "size" in q:
            print(ll.getSize())
            
        elif "removeFirst" in q:
            ll.removeFirst()
        elif "removeLast" in q:
            ll.removeLast()
        elif "removeAt" in q:
            idx = int(q.split()[1])
            val = ll.removeAt(idx)
            
        elif "getFirst" in q:
            val = ll.getFirst()
            if val!=-1:
                print(val)
        elif "getLast" in q:
            val = ll.getLast()
            if val!=-1:
                print(val)
        elif "getAt" in q:
            idx = int(q.split()[1])
            val = ll.getAt(idx)
            if val!=-1:
                print(val)
        
        elif "reverseDI" in q:
            ll.reverseDI()
        elif "reversePI" in q:
            ll.reversePI()
    

driver()
