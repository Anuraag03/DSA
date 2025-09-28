class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def allTraversal(root):
    preOrder = []
    postOrder  = []
    inOrder = []

    stack = []
    stack.append((root,1))
    while stack:
        node,state = stack.pop()
        if state==1:
            preOrder.append(node.val)
            stack.append((node,2))
            if node.left:
                stack.append((node.left,1))
        elif state==2:
            inOrder.append(node.val)
            stack.append((node,3))
            if node.right:
                stack.append((node.right,1))
        else:
            postOrder.append(node.val)
    return (preOrder,postOrder,inOrder)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(allTraversal(root))
            