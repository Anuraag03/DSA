class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def reverseKGroups(head,k):
    def reverseLL(start,end):
        prev = end
        curr = start
        while curr!=end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    dummy = ListNode()
    dummy.next = head
    prevGroup = dummy
    while True:
        curr = prevGroup
        for _ in range(k):
            curr=curr.next
            if not curr:
                return dummy.next
        nextGroup = curr.next
        newHead = reverseLL(prevGroup.next,nextGroup)

        tail = prevGroup.next
        prevGroup.next = newHead
        prevGroup = tail



# --- Helpers ---
def buildList(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def printList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

# --- Example Run ---
head = buildList([1, 2, 3, 4, 5])
print("Original List:")
printList(head)

k = 2
newHead = reverseKGroups(head, k)
print(f"Reversed in groups of {k}:")
printList(newHead)