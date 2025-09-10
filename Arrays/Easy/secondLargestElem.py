def secondLargestElem(nums):
    maxElem = float('-inf')
    secondMaxElem = float('-inf')
    for i in range(len(nums)):
        if nums[i]>maxElem:
            secondMaxElem = maxElem
            maxElem = nums[i]
        elif nums[i]<maxElem and nums[i]>secondMaxElem:
            secondMaxElem=nums[i]
    return secondMaxElem

nums = [1,4,2,5,7,3,6]
print(secondLargestElem(nums))