def moveZerosToEnd(nums):
    ind = -1
    for i,val in enumerate(nums):
        if val==0:
            ind = i
            break
    if ind == -1:
        return
    for k in range(i+1,len(nums)):
        if nums[k]!=0:
            nums[k],nums[ind] = nums[ind],nums[k]
            ind+=1

nums = [ 0,1,2,0,1,0,1,1]
moveZerosToEnd(nums)
print(nums) 