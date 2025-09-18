'''
Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. 
At a time the frog can climb either one or two steps. A height[N] array is also given. 
Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), 
where abs() means the absolute difference. 
We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.
'''

def frogJumpM(n,height):
    dp = [-1]*n
    def rec(num):
        if num==0:
            return 0
        jump1 = rec(num-1)+abs(height[num]-height[num-1])
        jump2 = float('inf')
        if num>1:
            jump2 = rec(num-2)+abs(height[num]-height[num-2])
        dp[num] = min(jump1,jump2)
        
        return dp[num]
    return rec(n-1)

def frogJumpT(n,height):
    dp = [0]*n
    for i in range(1,n):
        jump1 = dp[i-1]+abs(height[i-1]-height[i])
        jump2 = float('inf')
        if i >1:
            jump2 = dp[i-2]+abs(height[i-2]-height[i])
        dp[i] = min(jump1,jump2)
    return dp[n-1]

def frogJumpS(n,height):
    prev = 0
    prev2 = 0
    for i in range(1,n):
        jump1 = prev+abs(height[i-1]-height[i])
        jump2 = float('inf')
        if i>1:
            jump2 = prev2+abs(height[i-2]-height[i])
        prev2,prev = prev,min(jump1,jump2)
    return prev

height = [30,10,60 , 10 , 60 , 50]
n = 6
print(frogJumpM(n,height))
print(frogJumpT(n,height))
print(frogJumpS(n,height))