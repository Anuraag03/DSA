def floor(nums,target):# largest element smaller than or equal to target
    l = 0
    h = len(nums)-1
    maxi = -1
    while l<=h:
        mid = (l+h)//2
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid]<target:
            maxi = nums[mid]
            l = mid+1
        else:
            h = mid-1
    return maxi

def ceil(nums,target): #smallest element larger than or equal to target
    l = 0
    h = len(nums)-1
    ans = -1
    while l<=h:
        mid = (l+h)//2
        if nums[mid] == target:
            return nums[mid]
        if nums[mid]>target:
            ans = nums[mid]
            h=mid-1
        else:
            l=mid+1
    return ans
nums = [1,2,4,6,8]
print(floor(nums,3))
print(ceil(nums,3))