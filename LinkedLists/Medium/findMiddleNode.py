class Node():
    def __init__(self,next=None,val=None):
        self.next = next
        self.val = val

def findMiddleNode(head):
    slow = head
    fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


head = Node(val=1)
head.next = Node(val=2)
head.next.next = Node(val=3)
head.next.next.next = Node(val=4)
head.next.next.next.next = Node(val=5)

mid = findMiddleNode(head)
print(mid.val)