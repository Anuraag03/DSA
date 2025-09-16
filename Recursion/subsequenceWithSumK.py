def subsequenceWithSumK(nums,k): # TC: O(nx2^n), SC: O(nx2^n)
    res = []
    def rec(n,ans,currSum):
        if n == len(nums):
            if currSum == k:
                res.append(ans[:])
            return
        if currSum>k:
            return
        ans.append(nums[n])
        rec(n+1,ans,currSum+nums[n])
        ans.pop()
        rec(n+1,ans,currSum)
    rec(0,[],0)
    return res

nums = [4, 9, 2, 5, 1] 
k = 10
print(subsequenceWithSumK(nums,k))