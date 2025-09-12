'''
a peak element is an element that is strictly greater than its neighbours
'''

def peakElem(nums):
    l = 0
    h = len(nums)-1
    while l<h:
        mid = (l+h)//2
        if nums[mid]>nums[mid+1]:
            h = mid
        else:
            l = mid+1
    return nums[l]

print(peakElem([1,2,3,0]))

        