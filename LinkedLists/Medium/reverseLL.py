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

head = Node(val=1)
head.next = Node(val=2)
head.next.next = Node(val=3)
head.next.next.next = Node(val=4)
head.next.next.next.next = Node(val=5)

newHead = reverseLL(head)
while newHead:
    print(newHead.val)
    newHead = newHead.next


