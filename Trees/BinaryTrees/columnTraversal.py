from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def columnTraversal(root): #TC : O(N) and SC:O(N)
    if not root:
        return []
    column_map = {}
    q = deque()
    q.append((root,0))
    min_col, max_col = 0, 0
    while q:
        node,col = q.popleft()
        min_col = min(min_col,col)
        max_col = max(max_col,col)
        if col not in column_map:
            column_map[col] = [node.val]
        else:
            column_map[col].append(node.val)
        if node.left:
            q.append((node.left,col-1))
        if node.right:
            q.append((node.right,col+1))
    return [column_map[c] for c in range(min_col,max_col+1)]
def dfsColumnTraversal(root): # TC: O(nlogn) and SC: O(n)
    col_map = {}
    minMaxCol = [0, 0]

    def dfs(node, row, col):
        if not node:
            return
        if col not in col_map:
            col_map[col] = [(row, node.val)]
        else:
            col_map[col].append((row, node.val))

        # track min & max column index
        minMaxCol[0] = min(minMaxCol[0], col)
        minMaxCol[1] = max(minMaxCol[1], col)

        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)

    result = []
    for c in range(minMaxCol[0], minMaxCol[1] + 1):
        # sort by row first, then value
        col_map[c].sort(key=lambda x: (x[0], x[1]))
        result.append([val for row, val in col_map[c]])
    return result

        


#        20
#       /  \
#     8     22
#    / \      \
#   4  12      25
#      /  \
#     10  14


root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(4)
root.left.right = TreeNode(12)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)
root.right.right = TreeNode(25)

print(columnTraversal(root))
print(dfsColumnTraversal(root))