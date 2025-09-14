class Node():
    def __init__(self,next=None,val=None):
        self.next = next
        self.val = val

def reverseLL(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def addTwoNumbers(l1,l2): # Assuming the numbers 567 is denoted as 5->6->7->None
    newL1 = reverseLL(l1)
    newL2 = reverseLL(l2)
    carry = 0
    temp1 = newL1
    temp2 = newL2
    dummy = Node()
    temp = dummy
    while temp1 or temp2 or carry:
        currSum = 0
        if temp1:
            currSum+=temp1.val
            temp1 = temp1.next
        if temp2:
            currSum+=temp2.val
            temp2 = temp2.next
        if carry:
            currSum+=carry
        carry = currSum//10
        currSum%=10
        temp.next = Node(None,currSum)
        temp = temp.next
    return reverseLL(dummy.next)


# 567 (5->6->7) + 89 (8->9) = 656
l1 = Node(val=5, next=Node(val=6, next=Node(val=7)))
l2 = Node(val=8, next=Node(val=9))

res = addTwoNumbers(l1, l2)

# Print result
while res:
    print(res.val, end="->")
    res = res.next


        
        

