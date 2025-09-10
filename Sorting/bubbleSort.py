def bubbleSort(nums): #TC = O(N^2)
    for i in range(len(nums)-1,-1,-1):
        for j in range(0,i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

nums = [5,2,1,3,4,6]
bubbleSort(nums)
print(nums)

