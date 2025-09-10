def nextPermutation(nums):
    ind = -1
    for i in range(len(nums)-2,-1,-1):
        if nums[i]<nums[i+1]:
            ind = i
            break
    if ind==-1:
        return reversed(nums)
    for j in range(len(nums)-1,-1,-1):
        if nums[ind]<nums[j]:
            nums[ind],nums[j] = nums[j],nums[ind]
            break
    nums[ind+1:] = reversed(nums[ind+1:])
    return nums

print(nextPermutation([1,3,4,2]))

    