class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxPathSum(root):
    maxSum = [float('-inf')]
    def dfs(root):
        if not root:
            return 0
        
        lmax = max(dfs(root.left),0)
        rmax = max(dfs(root.right),0)
        maxSum[0] = max(maxSum[0],root.val+lmax+rmax)
        return root.val+max(lmax,rmax)
    dfs(root)
    return maxSum[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(maxPathSum(root))