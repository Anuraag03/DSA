def checkIfArraySortedRotated(nums): #TC = O(N)
    count = 0
    for i in range(len(nums)):
        if nums[i]>nums[(i+1)%len(nums)]:
            count+=1
    return count<=1

def findRotationPoint(nums): #TC = O(logn), the smallest elem is the rotation point, index of the smallest elem is no of rotations 
    low = 0
    high = len(nums)-1
    while low<high:
        mid = (low+high)//2
        if nums[mid]<nums[high]:
            high = mid
        else:
            low = mid+1
    return nums[low],low


nums = [6,1,2,3,4,5]
print(checkIfArraySortedRotated(nums))
res = findRotationPoint(nums)
print(f'Elem: {res[0]}'+' '+f'Index: {res[1]}')