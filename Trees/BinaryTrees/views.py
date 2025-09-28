from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def topView(root):

    if not root:
        return []
    q = deque()
    q.append((root,0))
    hd_map = {}
    while q:
        node,col = q.popleft()
        if col not in hd_map:
            hd_map[col] = node.val
        if node.left:
            q.append((node.left,col-1))
        if node.right:
            q.append((node.right,col+1))
    return [hd_map[x] for x in sorted(hd_map)]

def bottomView(root):

    if not root:
        return []
    q = deque()
    hd_map = {}
    q.append((root,0))
    while q:
        node,col = q.popleft()
        hd_map[col] = node.val
        if node.left:
            q.append((node.left,col-1))
        if node.right:
            q.append((node.right,col+1))
    return [hd_map[x] for x in sorted(hd_map)]

def leftView(root):
    if not root:
        return []
    q = deque([root]) #when initializing a value in deque, initialize inside []
    res = []
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i == 0:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res

def rightView(root):
    if not root:
        return []
    q = deque([root]) #when initializing a value in deque, initialize inside []
    res = []
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i == size-1:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res

#        20
#       /  \
#     8     22
#    / \      \
#   4  12      25
#      /  \
#     10  14


root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(4)
root.left.right = TreeNode(12)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)
root.right.right = TreeNode(25)

print("Top View   :", topView(root))
print("Bottom View   :", bottomView(root))
print("Left View :", leftView(root) )
print("Right View :", rightView(root) )
