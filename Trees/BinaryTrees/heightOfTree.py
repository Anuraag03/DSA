from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recHeightOfTree(root):
    if not root:
        return 0
    lh = recHeightOfTree(root.left)
    rh = recHeightOfTree(root.right)
    return max(lh,rh)+1
def heightOfTree(root):
    q = deque()
    if not root:
        return 0
    depth = 0
    q.append(root)
    while q:
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth+=1
    return depth




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(heightOfTree(root))
print(recHeightOfTree(root))