def longestSubarrayWithSumKPositives(nums,k):#TC = O(N) SC =O(1)
    l = 0
    r = 0
    sum = 0
    maxLen = 0
    for r in range(len(nums)):
        sum+=nums[r]
        if sum>k:
            sum-=nums[l]
            l+=1
        if sum == k:
            maxLen = max(maxLen,r-l+1)

        
        
    return maxLen

def longestSubarrayWithSumK(nums,k):
    prefixSum = {0:-1}
    maxLen = 0
    currSum = 0
    for i in range(len(nums)):
        currSum += nums[i]
        if currSum-k in prefixSum:
            maxLen = max(maxLen,i-prefixSum[currSum-k])
        if currSum not in prefixSum:
            prefixSum[currSum] = i
    return maxLen

def subarraysWithSumK(nums,k):
    prefixSum = {0:[-1]}
    currSum = 0
    res = []
    for i in range(len(nums)):
        currSum+=nums[i]
        for j in prefixSum[currSum-k]:
            res.append(nums[j+1:i+1])
        if currSum in prefixSum:
            prefixSum[currSum].append(i)
        else:
            prefixSum[currSum] = [i]
    return res

nums = [2, 3, 5, 1, 9]
k = 10
nums2 = [-1,0,1,1,0,-1,2]
k = 0
print(longestSubarrayWithSumKPositives(nums,k))
print(longestSubarrayWithSumK(nums2,k))
