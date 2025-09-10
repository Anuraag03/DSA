def kadanesAlgo(nums):
    maxSum = nums[0]
    currSum = nums[0]
    for i in range(1,len(nums)):
        currSum+=nums[i]
        maxSum=max(maxSum,currSum)
        if currSum<0:
            currSum = 0
    return maxSum

print(kadanesAlgo([-3, -5, -2])) 