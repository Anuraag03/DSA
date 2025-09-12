'''
Works only on sorted arrays, TC=O(logn) SC=O(1)
'''
def binarySearch(nums,target):
    low = 0
    high = len(nums)-1
    
    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid,nums[mid]
        elif mid<target:
            low+=1
        else:
            high-=1
    return -1,-1

def lowerBound(nums,target): #first/smallest index with elem that is >=target
    low = 0
    high = len(nums)-1
    ind = -1
    while low<=high:
        mid = (low+high)//2
        if nums[mid] >= target:
            ind = mid
            high=mid-1
        else:
            low = mid+1
    return ind

def upperBound(nums,target): #first/smallest index with elem that is >target
    low = 0
    high = len(nums)-1
    ind = -1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>target:
            ind = mid
            high = mid-1
        else:
            low = mid+1
    return ind
nums = [1,2,3,4,5,7]
print(binarySearch(nums,3))
print(lowerBound(nums,3))
print(upperBound(nums,5))