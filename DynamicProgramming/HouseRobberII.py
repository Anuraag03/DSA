'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically 
contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

 
'''

def rob(nums):
    if len(nums)==1:
        return nums[0]
    if len(nums)==0:
        return 0
    def solve(nums):
        n = len(nums)
        if n == 0:
            return 0
        if n==1:
                return nums[0]
        dp = [0]*(n)

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            sum1 = dp[(i-1)]
            sum2 = dp[(i-2)]+nums[i]
            dp[i] = max(sum1,sum2)
        return dp[n-1]
    return max(solve(nums[:-1]),solve(nums[1:]))
nums = [1,2,3,1]
print(rob(nums))