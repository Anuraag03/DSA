'''
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''
def combinationSumII(nums,k): #TC: O(2^nxn), SC :O(2^nxn)
    nums.sort()
    res = []
    def rec(n,ans,currSum):
        if currSum == k:
            res.append(ans[:])
            return
        if currSum>k:
            return
        for i in range(n,len(nums)):
            if i>n and nums[i]==nums[i-1]:
                continue
            ans.append(nums[i])
            rec(i+1,ans,currSum+nums[i])
            ans.pop()
    rec(0,[],0)
    return res

candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSumII(candidates,target))