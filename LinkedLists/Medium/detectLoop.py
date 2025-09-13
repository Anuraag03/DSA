class Node():
    def __init__(self,next=None,val=None):
        self.next = next
        self.val = val

def detectLoop(head):
    slow = head 
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

def findStartOfLoop(head):
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            slow = head
            break
    else:
        return -1 #no cycle
    while fast!=slow:
        slow=slow.next
        fast=fast.next
    return slow.val

def lengthOfLoop(head):
    slow = head
    fast = head
    counter = 0
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            slow = slow.next
            counter+=1
            break
    else:
        return -1 #no cycle
    while fast!=slow:
        slow = slow.next
        counter+=1
    return counter

head = Node(val=1)
head.next = Node(val=2)
head.next.next = Node(val=3)
head.next.next.next = Node(val=4)
head.next.next.next.next = head.next


print(detectLoop(head))
print(findStartOfLoop(head))
print(lengthOfLoop(head))