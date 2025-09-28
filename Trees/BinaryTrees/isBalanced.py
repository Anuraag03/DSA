from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def checkHeight(root):
    if not root:
        return 0
    left = checkHeight(root.left)
    if left==-1:
        return -1
    right = checkHeight(root.right)
    if right == -1:
        return -1
    if abs(left-right)>1:
        return -1
    return max(left,right)+1

def isBalanced(root):
    return checkHeight(root) != -1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)
root.left.right.right.right = TreeNode(7)

print(isBalanced(root))