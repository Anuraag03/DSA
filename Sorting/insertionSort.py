def insertionSort(nums): # TC = O(N^2)
    for i in range(1,len(nums)):
        k = i
        while k and nums[k-1]>nums[k]:
            nums[k-1],nums[k] = nums[k],nums[k+1]
            k-=1
nums = [5,2,1,3,4,6]
insertionSort(nums)
print(nums)        
        