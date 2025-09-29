def kadanesAlgo(nums):
    maxSum = nums[0]
    currSum = nums[0]
    for i in range(1, len(nums)):
        currSum = max(nums[i], currSum + nums[i])  # either start fresh or extend
        maxSum = max(maxSum, currSum)
    return maxSum

def maxSumSubarray(nums):
    maxSum = nums[0]
    currSum = nums[0]
    start = 0
    temp = 0
    end = 0
    for i in range(1,len(nums)):
        if nums[i]>currSum+nums[i]:
            currSum = nums[i]
            tempStart  = i
        else:
            currSum+=nums[i]
        if currSum>maxSum:
            start = tempStart
            end = i
            maxSum = currSum
    return nums[start:end+1]


nums = [-3, -5, -2, 1, 1, 1]
print(kadanesAlgo(nums)) 
print(maxSumSubarray(nums))