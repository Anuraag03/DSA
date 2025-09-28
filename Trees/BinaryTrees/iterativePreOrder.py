class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def iterativePreOrder(root):
    stack = []
    res = []
    if not root:
        return
    stack.append(root)
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(iterativePreOrder(root))