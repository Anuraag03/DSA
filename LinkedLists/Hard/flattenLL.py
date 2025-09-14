'''
Problem Statement: Given a linked list containing 'N' head nodes where every node in the linked list contains two pointers:
'Next' points to the child node in the list
'Child' pointer to a linked list where the current node is the head
Each of these child linked lists is in sorted order and connected by a 'child' pointer. 
Your task is to flatten this linked list such that all nodes appear in a single layer or level in a 'sorted order'.
'''
class ListNode:
    def __init__(self, val=None, next=None,child = None):
        self.val = val
        self.next = next
        self.child = child

def merge(l1,l2):
    dummy = ListNode()
    temp = dummy
    temp1 = l1
    temp2 = l2
    while temp1 and temp2:
        if temp1.val<=temp2.val:
            temp.child = temp1
            temp = temp.child
            temp1 = temp1.child
        else:
            temp.child = temp2
            temp = temp.child
            temp2 = temp2.child
    temp.child = temp1 or temp2
    return dummy.child
def flattenLL(head):
    if not head or not head.next:
        return head

    mergedHead = flattenLL(head.next)
    return merge(head,mergedHead) 

def print_flattened_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.child
    print(res)


if __name__ == "__main__":
    # Build sample list
    head = ListNode(5)
    head.child = ListNode(7, child=ListNode(8))

    head.next = ListNode(10)
    head.next.child = ListNode(20)

    head.next.next = ListNode(19)
    head.next.next.child = ListNode(22, child=ListNode(50))

    head.next.next.next = ListNode(28)
    head.next.next.next.child = ListNode(35, child=ListNode(40, child=ListNode(45)))

    # Flatten and print
    flat = flattenLL(head)
    print_flattened_list(flat)

