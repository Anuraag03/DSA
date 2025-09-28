class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def inorderTraversal(root):
    stack, result = [], []
    curr = root
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        node = stack.pop()
        result.append(node.val)
        curr = node.right
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(inorderTraversal(root))

