class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
    diameter = [0]
    def heightOfTree(root):
        if not root:
            return 0
        lh = heightOfTree(root.left)
        rh = heightOfTree(root.right)
        diameter[0] = max(diameter[0],lh+rh)
        return max(lh,rh)+1
    heightOfTree(root)
    return diameter[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(diameterOfBinaryTree(root))