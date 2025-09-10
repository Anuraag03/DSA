def largestElem(nums):
    maxElem = nums[0]
    for i in range(1,len(nums)):
        if nums[i]>maxElem:
            maxElem = nums[i]
    return maxElem

nums = [1,5,6,2,1,3]
print(largestElem(nums))