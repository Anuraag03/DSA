'''
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is 
less than 150 combinations for the given input.
'''
def combinationSum(nums,k):
    res = []
    def rec(n,ans,currSum):
        if currSum == k:
            res.append(ans[:])
            return
        if currSum>k:
            return
        for i in range(n,len(nums)):
            ans.append(nums[i])
            rec(i,ans,currSum+nums[i])
            ans.pop()
    rec(0,[],0)
    return res

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates,target))
