class Node():
    def __init__(self,next=None,val=None):
        self.next = next
        self.val = val
def merge(l,r):
    dummy = Node()
    temp = dummy
    while l and r:
        if l.val<=r.val:
            temp.next = l
            temp = temp.next
            l = l.next
        else:
            temp.next = r
            temp = temp.next
            r = r.next
    temp.next = l or r
    return dummy.next
def sortLL(head):
    if not head or not head.next:
        return head
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    prev.next = None
    l = sortLL(head)
    r = sortLL(slow)
    return merge(l,r)

head = Node(val=5)
head.next = Node(val=2)
head.next.next = Node(val=3)
head.next.next.next = Node(val=1)
head.next.next.next.next = Node(val=4)

newHead = sortLL(head)

while newHead:
    print(newHead.val,end="->")
    newHead = newHead.next