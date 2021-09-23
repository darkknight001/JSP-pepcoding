class Stack:
    def __init__(self):
        self.storage = []
        self.top = None
    
    def push(self, num):
        self.storage.append(num)
        
    def pop(self):
        num = self.storage.pop()
        return num
    
    def peek(self):
        return self.storage[-1]
    
    def size(self):
        return len(self.storage())