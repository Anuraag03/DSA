def dutchNationalFlag(nums):
    l=0
    m=0
    r=len(nums)-1
    while m<r:
        if nums[m]==0:
            nums[m],nums[l] = nums[l],nums[m]
            l+=1
            m+=1
        elif nums[m]==1:
            m+=1
        else:
            nums[r],nums[m] = nums[m],nums[r]
            r-=1

nums = [0,2,1,0,2,1,2,1,0,2,0]
dutchNationalFlag(nums)
print(nums)