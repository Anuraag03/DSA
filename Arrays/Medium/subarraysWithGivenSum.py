def countSubarrayWithSum(nums,k): #TC O(N) and SC = O(N)
    currSum = 0
    prefixSum = {0:1}
    count = 0
    for i in range(len(nums)):
        currSum+=nums[i]
        if currSum-k in prefixSum:
            count+=prefixSum[currSum-k]
        prefixSum[currSum] = prefixSum.get(currSum,0)+1
    return count

def subarrayWithSumK(nums,k):
    currSum = 0
    prefixSum = {0:[-1]}
    res = []
    for i in range(len(nums)):
        currSum+=nums[i]
        if currSum-k in prefixSum:
            for j in prefixSum[currSum-k]:
                res.append(nums[j+1:i+1])
        if currSum in prefixSum:
            prefixSum[currSum].append(i)
        else:
            prefixSum[currSum] = [i]
    return res
nums = [3, 1, 2, 4]
print(countSubarrayWithSum(nums,6))
nums2 = [-1,0,1,1,0,-1,2]
k = 0
print(subarrayWithSumK(nums2,k))
