class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Given a Binary Search Tree and a key, return the ceiling of the given key in the Binary Search Tree.
Ceiling of a value refers to the value of the smallest node in the Binary Search Tree 
that is greater than or equal to the given key.
If the ceiling node does not exist, return None.
'''

def findCeil(root,target):
    if not root:
        return None
    node = root
    res = None
    while node:
        if node.val==target:
            return node.val
        if node.val>target:
            res = node.val
            node = node.left
        else:
            node = node.right
    return res

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

print('Ceil: ',findCeil(root,15))
