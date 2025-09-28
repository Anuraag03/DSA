class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def iterativePostOrder(root):
    if not root:
        return []   
    st1,st2 = [],[]
    st1.append(root)
    while st1:
        node = st1.pop()
        st2.append(node.val)
        if node.left:
            st1.append(node.left)
        if node.right:
            st1.append(node.right)
    
    return st2[::-1]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(iterativePostOrder(root))