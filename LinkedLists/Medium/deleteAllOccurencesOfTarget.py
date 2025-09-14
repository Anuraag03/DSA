class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def deleteAllOccurrences(head, target):
    temp = head
    while temp:
        if temp.val == target:
            if temp == head:
                head = temp.next
                if head:  
                    head.prev = None
            else:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
        temp = temp.next  
    return head

# Create DLL: 1 <-> 2 <-> 3 <-> 2 <-> 4
head = ListNode(1)
n2 = ListNode(2); head.next = n2; n2.prev = head
n3 = ListNode(3); n2.next = n3; n3.prev = n2
n4 = ListNode(2); n3.next = n4; n4.prev = n3
n5 = ListNode(4); n4.next = n5; n5.prev = n4

# Print DLL utility
def printDLL(head):
    temp = head
    while temp:
        print(temp.val, end=" <-> " if temp.next else "")
        temp = temp.next
    print()

print("Original DLL:")
printDLL(head)

# Delete all occurrences of 2
head = deleteAllOccurrences(head, 2)

print("After deleting 2:")
printDLL(head)
