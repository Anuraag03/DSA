from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def boundaryTraversal(root):
    res = []
    if not root:
        return res
    def isLeaf(node):
        return not node.left and not node.right
    def leftBoundary(node):
        curr = node.left
        while curr:
            if not isLeaf(curr):
                res.append(curr.val)
            if curr.left:
                curr=curr.left
            else:
                curr=curr.right
    def rightBoundary(node):
        curr = node.right
        temp = []
        while curr:
            if not isLeaf(curr):
                temp.append(curr.val)
            if curr.right:
                curr=curr.right
            else:
                curr=curr.left
        for i in range(len(temp)-1,-1,-1):
            res.append(temp[i])
    def addLeaves(node):
        if not node:
            return
        if isLeaf(node):
            res.append(node.val)
            return
        addLeaves(node.left)
        addLeaves(node.right)

    if not isLeaf(root):
        res.append(root.val)
    
    leftBoundary(root)
    addLeaves(root)
    rightBoundary(root)
    return res

root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(4)
root.left.right = TreeNode(12)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)
root.right.right = TreeNode(25)

print(boundaryTraversal(root))