def genAllSubarrays(nums): #TC :O(nx2^n) SC : O(nx2^n)
    res = []
    def rec(n,ans):
        res.append(ans[:])
        for i in range(n,len(nums)):
            ans.append(nums[i])
            rec(i+1,ans)
            ans.pop()
    rec(0,[])
    return res

print(genAllSubarrays([1,2,3,4,5]))