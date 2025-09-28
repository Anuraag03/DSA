# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    direction = 0
    q = deque()
    q.append(root)
    res = []
    if not root:
        return res
    while q:
        size = len(q)
        level = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if direction == 1:
            level.reverse()
        res.append(level)

        direction ^= 1
    return res
                    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(zigzagLevelOrder(root))
                    

