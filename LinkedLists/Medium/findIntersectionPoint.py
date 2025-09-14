class Node():
    def __init__(self,next=None,val=None):
        self.next = next
        self.val = val
def findIntersectionPoint(l1,l2):
    p1 = l1
    p2 = l2
    while p1!=p2:
        p1 = p1.next if p1 else l2
        p2 = p2.next if p2 else l1
    return p1

# Build shared part
shared = Node(val=8)
shared.next = Node(val=9)
shared.next.next = Node(val=10)

# Build first list: 1 -> 2 -> 8 -> 9 -> 10
l1 = Node(val=1)
l1.next = Node(val=2)
l1.next.next = shared

# Build second list: 3 -> 4 -> 8 -> 9 -> 10
l2 = Node(val=3)
l2.next = Node(val=4)
l2.next.next = shared

# Run intersection finder
res = findIntersectionPoint(l1, l2)

print("Intersection at node with value:", res.val if res else None)
