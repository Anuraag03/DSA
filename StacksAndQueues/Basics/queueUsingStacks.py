class Queue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self,x):
        while self.inStack:
            self.outStack.append(self.inStack.pop())
        self.inStack.append(x)
        while self.outStack:
            self.inStack.append(self.outStack.pop())
    def pop(self):
        return self.inStack.pop()
    def top(self):
        return self.inStack[-1]
    def isEmpty(self):
        return len(self.inStack) == 0
    
q = Queue()
print(q.isEmpty())
q.push(1)
q.push(2)
q.push(3)
print(q.pop())
print(q.top())
