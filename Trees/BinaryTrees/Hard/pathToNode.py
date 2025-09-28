class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathToNode(root,node):#TC: O(n) SC:O(h) h = height of tree
    res = []
    def dfs(start):
        if not start:
            return False
        res.append(start.val)
        if start.val == node:
            return True
        

        if dfs(start.left) or dfs(start.right):
            return True
        res.pop()
        return False

    dfs(root)
    return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(pathToNode(root,4))



