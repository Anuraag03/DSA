def findMinimum(nums): #find minimum in rotated sorted array, the index of the min elem is also the rotation point
    l = 0
    h = len(nums)-1
    while l<h:
        mid = (l+h)//2
        if nums[mid]<=nums[h]:
            h = mid-1
        else:
            l = mid+1
    return nums[l]

def findRotationPoint(nums): # l is the rotation point as well as number of rotations
    l = 0
    h = len(nums)-1
    while l<h:
        mid = (l+h)//2
        if nums[mid]<=nums[h]:
            h = mid-1
        else:
            l = mid+1
    return l



nums = [6,7,0,1,2,3,4,5]
print(findMinimum(nums))
print(findRotationPoint(nums))
        