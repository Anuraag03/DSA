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

def threeSumIndex(nums,k):
    res = []
    numsWithIndex = [(num,i) for i,num in enumerate(nums) ]
    numsWithIndex.sort(key=lambda x: x[0])

    for i in range(len(numsWithIndex)):
        if i>0 and numsWithIndex[i][0] == numsWithIndex[i-1][0]:
            continue
        l = i+1
        r = len(numsWithIndex)-1
        while l<r:
            currSum = numsWithIndex[i][0]+numsWithIndex[l][0]+numsWithIndex[r][0]
            if currSum<k:
                l+=1
            elif currSum>k:
                r-=1
            else:
                res.append([numsWithIndex[i][1],numsWithIndex[l][1],numsWithIndex[r][1]])
                while l<r and numsWithIndex[l][0] == numsWithIndex[l+1][0]:
                    l+=1
                while l<r and numsWithIndex[r][0] == numsWithIndex[r-1][0]:
                    r-=1
                l+=1
                r-=1
    return res 



nums = [-1,0,1,2,-1,-4]
#print(threeSum(nums,0))
print(threeSumIndex(nums,0))