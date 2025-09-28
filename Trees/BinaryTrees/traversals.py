# inorder = left->root->right
# preorder = root->left->right
# postorder = left->right->root
# levelorder = level wise

from collections import deque
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def preOrder(root):
    arr = []
    def rec(root,arr):
        if not root:
            return
        arr.append(root.data)
        rec(root.left,arr)
        rec(root.right,arr)
    rec(root,arr)
    return arr

def postOrder(root):
    arr = []
    def rec(root,arr):
        if not root:
            return
        
        rec(root.left,arr)
        rec(root.right,arr)
        arr.append(root.data)
    rec(root,arr)
    return arr

def inOrder(root):
    arr = []
    def rec(root,arr):
        if not root:
            return
        
        rec(root.left,arr)
        arr.append(root.data)
        rec(root.right,arr)
        
    rec(root,arr)
    return arr


def levelOrder(root):
    ans = []
    if not root:
        return ans
    
    q = deque()
    q.append(root)
    while q:
        size = len(q)
        level = []
        for i in range(size):
            node = q.popleft()
            level.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(preOrder(root))
    print(postOrder(root))
    print(inOrder(root))
    print(levelOrder(root))


