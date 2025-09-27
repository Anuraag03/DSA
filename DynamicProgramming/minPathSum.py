'''
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
'''
def minPathSumM(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[-1]*n for _ in range(m)]
    def rec(row,col):
        if row==0 and col == 0:
            return grid[row][col]
        if dp[row][col]!=-1:
            return dp[row][col]
        up = rec(row-1,col) if row>0 else float('inf')
        left = rec(row,col-1) if col>0 else float('inf')
        dp[row][col] = grid[row][col]+min(up,left)
        return dp[row][col]
    return rec(m-1,n-1)

def minPathSumT(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                continue
            up = dp[i-1][j] if i>0 else float('inf')
            left = dp[i][j-1] if j>0 else float('inf')
            dp[i][j] = grid[i][j]+min(up,left)
    return dp[m-1][n-1]


grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSumM(grid))
print(minPathSumT(grid))
