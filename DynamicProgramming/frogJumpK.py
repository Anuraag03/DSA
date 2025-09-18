def frogJumpsKM(n,k,height): #TC: O(N*K) SC:O(N)
    dp = [-1]*(n)

    def rec(num):
        if num == 0:
            return 0
        if dp[num]!=-1:
            return dp[num]
        minJump = float('inf')
        for j in range(1,k+1):
        
            if num-j>=0:
                jump = rec(num-j)+abs(height[num]-height[num-j])
                minJump = min(jump,minJump)
        dp[num] = minJump
        return dp[num]
    return rec(n-1)

def frogJumpsKT(n,k,height):#TC: O(N*K) SC:O(N)
    dp = [0]*(n)
    for i in range(1,n):
        minJump = float('inf')
        for j in range(1,k+1):
            if i-j>=0:
                jump = dp[i-j]+abs(height[i]-height[i-j])
                minJump = min(minJump,jump)
        dp[i] = minJump
    return dp[n-1]

# space optimization can be implemented by limiting the size of the dp array to the last k elems

height = [30, 10, 60, 10, 60, 50]
n = len(height)
k = 2
print(frogJumpsKM(n,k,height))
print(frogJumpsKT(n,k,height))
