def subsetSum(nums,target):
    res = []
    def rec(n,ans,total):
        if n == len(nums):
            if total==target:
                res.append(ans[:])
            return
        ans.append(nums[n])
        rec(n+1,ans,total+nums[n])
        ans.pop()
        rec(n+1,ans,total)
    rec(0,[],0)
    return res

def subsetSumM(nums,target):
    n = len(nums)
    dp = [[-1]*(target+1) for _ in range(n)]
    def rec(i,t):
        if t == 0:
            return True
        if i == 0:
            return nums[i]==t
        if dp[i][t]!=-1:
            return dp[i][t]
        not_take = rec(i-1,t)
        take = False
        if nums[i]<=t:
            take = rec(i-1,t-nums[i])
        
        dp[i][t] = take or not_take
        return dp[i][t]
    return rec(n-1,target)

def subsetSumTab(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n)]

    # Base cases
    for i in range(n):
        dp[i][0] = True   # sum 0 is always possible
    if nums[0] <= target:
        dp[0][nums[0]] = True

    for i in range(1, n):
        for t in range(1, target + 1):
            not_take = dp[i - 1][t]
            take = False
            if nums[i] <= t:
                take = dp[i - 1][t - nums[i]]
            dp[i][t] = take or not_take

    return dp[n - 1][target]

def subsetSumSO(nums, target):
    n = len(nums)
    prev = [False] * (target + 1)
    prev[0] = True

    if nums[0] <= target:
        prev[nums[0]] = True

    for i in range(1, n):
        curr = prev[:]  # or [False]*(target+1), but copying ensures correctness
        for t in range(target, nums[i] - 1, -1):
            curr[t] = prev[t] or prev[t - nums[i]]
        prev = curr
    return prev[target]


arr = [1, 2, 3, 4]
k = 4
print(subsetSum(arr,k))    
print(subsetSumM(arr,k))
