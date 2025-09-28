class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val!=q.val:
        return False
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(isSameTree(root,root2))