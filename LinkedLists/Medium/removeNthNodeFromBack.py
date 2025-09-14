class Node():
    def __init__(self,next=None,val=None):
        self.next = next
        self.val = val
def removeNthNodeFromBack(head,n):
    prev = None
    slow = head
    fast = head
    for _ in range(n):
        fast = fast.next
    while fast:
        fast = fast.next
        prev = slow
        slow = slow.next
    prev.next = slow.next

head = Node(val=1)
head.next = Node(val=2)
head.next.next = Node(val=3)
head.next.next.next = Node(val=4)
head.next.next.next.next = Node(val=5)
temp = head
while temp:
    print(temp.val)
    temp = temp.next
removeNthNodeFromBack(head,2)
temp = head
while temp:
    print(temp.val)
    temp = temp.next