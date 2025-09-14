'''
Given the head of a sorted doubly linked list of positive distinct integers, and a target integer, 
return a 2D array containing all unique pairs of nodes (a, b) such that a + b == target.
Each pair should be returned as a 2-element array [a, b] with a < b. 
The list is sorted in ascending order. If there are no such pairs, return an empty list.
'''

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def twoSum(head,k):
    left = head
    right = head
    res = []
    while right.next:
        right = right.next
    while left and right and left != right and left.prev != right:
        currSum = left.val+right.val
        if currSum==k:
            res.append([left.val,right.val])
            leftval = left.val
            while leftval == left.val:
                left = left.next
            rightval = right.val
            while rightval == right.val:
                right = right.prev
        elif currSum<k:
            left=left.next
        else:
            right=right.prev
    return res

# Build DLL: 1 <-> 2 <-> 2 <-> 3 <-> 4 <-> 4 <-> 5
head = ListNode(1)
n2a = ListNode(2); head.next = n2a; n2a.prev = head
n2b = ListNode(2); n2a.next = n2b; n2b.prev = n2a
n3 = ListNode(3); n2b.next = n3; n3.prev = n2b
n4a = ListNode(4); n3.next = n4a; n4a.prev = n3
n4b = ListNode(4); n4a.next = n4b; n4b.prev = n4a
n5 = ListNode(5); n4b.next = n5; n5.prev = n4b

# Call twoSum
print(twoSum(head, 6))

