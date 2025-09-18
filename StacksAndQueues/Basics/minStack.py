'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''

class MinStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self,val):
        if not self.stack2 or self.stack2[-1]>=val:
            self.stack2.append(val)
        self.stack1.append(val)
    def pop(self):
        val = self.stack1.pop()
        if val==self.stack2[-1]:
            self.stack2.pop()
        return val
    def top(self):
        return self.stack1[-1]
    def getMin(self):
        return self.stack2[-1]
    
m = MinStack()

m.push(-3)
m.push(1)
m.push(-2)

print(m.pop())
print(m.top())
print(m.getMin())


