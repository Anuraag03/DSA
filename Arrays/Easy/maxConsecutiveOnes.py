def maxConsecutiveOnes(nums):
    currCount = 0
    maxCount = 0
    for i in nums:
        if i:
            currCount+=1
        else:
            maxCount = max(maxCount,currCount)
            currCount = 0
    maxCount = max(maxCount,currCount)
    return maxCount

print(maxConsecutiveOnes([0,1,1,1,1,1,0,1,1,1,0,1,1,0,1,0]))