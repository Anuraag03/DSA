def first(nums,target):
    l = 0
    h = len(nums)-1
    ans = -1
    while l<=h:
        mid = (l+h)//2
        if nums[mid]==target:
            ans = mid
            h = mid-1
        elif nums[mid]<target:
            l=mid+1
        else:
            h=mid-1
    return ans

def last(nums,target):
    l = 0
    h = len(nums)-1
    ans = -1
    while l<=h:
        mid = (l+h)//2
        if nums[mid]==target:
            ans = mid
            l = mid+1
        elif nums[mid]>target:
            h = mid-1
        else:
            l = mid+1
    return ans
def firstAndLastAppearance(nums,target):
    f = first(nums,target)
    l = last(nums,target)
    return f,l

def countOccurences(nums,target):
    f = first(nums,target)
    l = last(nums,target)
    return l-f+1
nums = [1,2,2,2,3,4,5]
print(firstAndLastAppearance(nums,2))
print(countOccurences(nums,2))