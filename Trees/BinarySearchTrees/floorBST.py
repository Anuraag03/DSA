class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Given a Binary Search Tree and a key, return the floor of the given key in the Binary Search Tree.
Floor of a value refers to the value of the largest node in the Binary Search Tree 
that is smaller than or equal to the given key.
If the floor node does not exist, return nullptr.
'''

def findFloor(root,target):
    if not root:
        return None
    node = root
    res = None
    while node:
        if node.val==target:
            return node.val
        if node.val>target:
            node = node.left
        else :
            res = node.val
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

print('Ceil: ',findFloor(root,11))
