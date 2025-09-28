# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Your searchBST function
def searchBST(root, val):
    node = root
    while node:
        if node.val == val:
            return node
        if node.val < val:
            node = node.right
        else:
            node = node.left
    return None

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

# Search for a value
val_to_search = 6
found_node = searchBST(root, val_to_search)

if found_node:
    print(f"Node with value {val_to_search} found: {found_node.val}")
else:
    print(f"Node with value {val_to_search} not found.")
