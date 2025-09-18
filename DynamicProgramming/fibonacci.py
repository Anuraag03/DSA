def fib(num): #TC: O(2^n) SC: O(n)
    if num<=1:
        return num
    return fib(num-1)+fib(num-2)

def memoizationFib(num):#TC: O(n) SC:O(n)
    dp = [-1]*(num+1)
    def rec(num,dp):
        if num<=1:
            return num
        if dp[num]!=-1:
            return dp[num]
        dp[num] = rec(num-1,dp)+rec(num-2,dp)
        return dp[num]
    return rec(num,dp)

def tabulationFib(num):#TC: O(n) SC:O(n) but no recursion stack overhead
    if num<=1:
        return num

    dp = [0]*(num+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,num+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[num]

def spaceOptimizedFib(num): #TC: O(n) SC:O(1)
    if num<=1:
        return num
    prev1,prev2 = 0,1
    for i in range(2,num+1):
        curr = prev1+prev2
        prev1 = prev2
        prev2 = curr
    return prev2



print(fib(3))
print(memoizationFib(3))
print(tabulationFib(3))
print(spaceOptimizedFib(3))