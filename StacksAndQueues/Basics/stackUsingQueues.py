from collections import deque
class Stack:
    def __init__(self):
        self.q = deque()
    def push(self,x):
        self.q.append(x)
        l = len(self.q)
        while l>1:
            self.q.append(self.q.popleft())
            l-=1
    def pop(self):
        return self.q.popleft()
    def top(self):
        return self.q[0]
    def isEmpty(self):
        return len(self.q)==0
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.top())



