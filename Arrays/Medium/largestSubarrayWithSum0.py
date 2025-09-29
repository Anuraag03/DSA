def largestZeroSumSubarray(nums):
    currSum = 0
    prefixSum = {0:-1}
    maxLen = 0
    for i in range(len(nums)):
        currSum += nums[i]
        if currSum == 0:
            maxLen = max(maxLen,i+1)
        if currSum in prefixSum:
            maxLen = max(maxLen,i-prefixSum[currSum])
        else:
            prefixSum[currSum] = i
    return maxLen

nums = [1, 2, -2, 4, -4]

print(largestZeroSumSubarray(nums))