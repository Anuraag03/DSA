'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
# M = Memoization (top-down recursive approach)
# T = Tabulation (bottom-up iterative approach)
# S = Space Optimized
def climbStairsM(n):
    dp = [-1]*(n+1)
    def rec(num):
        if num<=1:
            return 1
        if dp[num]!=-1:
            return dp[num]
        dp[num] = rec(num-1)+rec(num-2)
        return dp[num]
    return rec(n)

def climbStairsT(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

def climbStairsS(n):
    prev,prev2 = 1,1
    for i in range(2,n+1):
        curr = prev+prev2
        prev,prev2 = prev2,curr
    return prev2
print(climbStairsM(4))
print(climbStairsT(4))
print(climbStairsS(4))