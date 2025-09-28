class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def findMin(root):
    node = root
    while node.left:
        node = node.left

    return node.val

def findMax(root):
    node = root
    while node.right:
        node = node.right
    return node.val

# Example BST:
#        8
#       / \
#      3   10
#     / \    \
#    1   6    14
#       / \   /
#      4   7 13

root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

print('Min Elem: ',findMin(root))
print('Max Elem: ',findMax(root))