'''
There is a robot on an m x n grid.
The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the 
robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''
def uniquePathsM(m, n):
    dp = [[-1]*n for _ in range(m)]
    def rec(row,col):
        if row<0 or col<0:
            return 0
        if row == 0 and col == 0:
            return 1
        if dp[row][col]!=-1:
            return dp[row][col]
        dp[row][col] = rec(row-1,col)+rec(row,col-1)
        return dp[row][col]
    return rec(m-1,n-1)

def uniquePathsT(m, n):
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for row in range(m):
            for col in range(n):
                if row==0 and col == 0:
                    continue
                up = dp[row-1][col] if row>0 else 0
                left = dp[row][col-1] if col>0 else 0
                dp[row][col] = up+left
        return dp[m-1][n-1]
 
print(uniquePathsM(3,3))
print(uniquePathsT(3,3))