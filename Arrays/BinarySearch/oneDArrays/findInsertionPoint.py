'''
Given an elem find the elem or find insert position if the element doesnot exit
'''
def findInsertPosition(nums,target):
    l = 0
    h = len(nums)-1
    while l<=h:
        mid = (l+h)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            h = mid-1
        else:
            l = mid+1
    return l

nums = [1,3,4,5]
print(findInsertPosition(nums,2))
print(findInsertPosition(nums,4))