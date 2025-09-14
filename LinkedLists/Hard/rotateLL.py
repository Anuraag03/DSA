class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
def rotateRight(head,k):
    if not head or not head.next or k == 0:
        return head
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length+=1
    k = k%length
    tail.next = head
    pointer = head
    for _ in range(length-k-1):
        pointer = pointer.next
    newHead = pointer.next
    pointer.next = None
    return newHead

def rotateLeft(head,k):
    if not head or not head.next or k == 0:
        return head
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length+=1
    k = k%length
    tail.next = head
    pointer = head
    for _ in range(k-1):
        pointer = pointer.next
    newHead = pointer.next
    pointer.next = None
    return newHead

# Helpers
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def linked_list_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


# Example run
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 2

    head1 = build_linked_list(nums)
    rotatedRight = rotateRight(head1, k)

    head2 = build_linked_list(nums)
    rotatedLeft = rotateLeft(head2, k)

    print("Input:", nums)
    print("k =", k)
    print("Right Rotation:", linked_list_to_list(rotatedRight))
    print("Left Rotation: ", linked_list_to_list(rotatedLeft))
