def selectionSort(nums): #TC = O(N^2)
    for i in range(len(nums)):
        mini = i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[mini]:
                mini = j
        nums[i],nums[mini] = nums[mini],nums[i]
    
            

        

nums = [5,2,3,6,1,4]
selectionSort(nums)
print(nums)

                