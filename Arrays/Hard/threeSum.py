def threeSum(nums,k):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        low = i+1
        high = len(nums)-1
        while low<high:
            sum = nums[i]+nums[low]+nums[high]
            if sum<k:
                low+=1
            elif sum>k:
                high-=1
            else:
                res.append([nums[i],nums[low],nums[high]])
                while low<high and nums[low] == nums[low+1]:
                    low+=1
                while low<high and nums[high]==nums[high-1]:
                    high-=1
                low+=1
                high-=1
    return res

