'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
'''
def subsets(nums):
    res = []
    nums.sort()
    def rec(n,ans):
        res.append(ans[:])
        for i in range(n,len(nums)):
            if i!=n and nums[i]==nums[i-1]:
                continue
            ans.append(nums[i])
            rec(i+1,ans)
            ans.pop()
    rec(0,[])
    return res

print(subsets([1,2,2]))