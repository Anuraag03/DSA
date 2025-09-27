'''
Given an array of N positive integers, we need to return the maximum sum of the subsequence such 
that no two elements of the subsequence are adjacent elements in the array.
Note: A subsequence of an array is a list with elements of the array where some elements 
are deleted ( or not deleted at all) and the elements should be in the same order in the subsequence as in the array.
'''
# Can solve House Robber problem with the below algo
def maxSumOfNonAdjacentM(n,nums):
    dp = [-1]*(n)
    def rec(num):
        if num == 0:
            return nums[0]
        if num == 1:
            return max(nums[0], nums[1])
        if dp[num]!=-1:
            return dp[num]
        sum1 = rec(num-1)
        sum2 = rec(num-2)+nums[num]
        dp[num] = max(sum1,sum2)
        return dp[num]
    return rec(n-1)

def maxSumOfNonAdjacentT(n,nums):
    if n == 1:
        return nums[0]
    dp = [0]*(n)
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    for i in range(2,n):
        sum1 = dp[i-1]
        sum2 = dp[i-2]+nums[i]
        dp[i] = max(sum1,sum2)
    return dp[n-1]

def maxSumOfNonAdjacentS(n,nums):
    if n == 1:
        return nums[0]
    prev2 = nums[0]
    prev = max(nums[0],nums[1])
    for i in range(2,n):
        sum1 = prev
        sum2 = prev2+nums[i]
        curr = max(sum1,sum2)
        prev2,prev = prev,curr
    return prev
nums = [2, 1, 4, 9]
n = len(nums)
print(maxSumOfNonAdjacentM(n,nums))
print(maxSumOfNonAdjacentT(n,nums))
print(maxSumOfNonAdjacentS(n,nums))
