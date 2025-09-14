class Node():
    def __init__(self,next=None,val=None):
        self.next = next
        self.val = val

def isPalindrome(head):
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    first = head
    second = prev
    while second:
        if first.val!=second.val:
            return False
        first = first.next
        second = second.next
    return True

head = Node(val=1)
head.next = Node(val=2)
head.next.next = Node(val=3)
head.next.next.next = Node(val=2)
head.next.next.next.next = Node(val=1)

print(isPalindrome(head))
    