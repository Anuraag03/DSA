'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.
'''
def kthMissingNumber(arr,k):
    l = 0
    r = len(arr)-1
    while l<=r:
        mid = (l+r)//2
        missing  = arr[mid]-(mid+1)
        if missing<k:
            l = mid+1
        else:
            r = mid-1
    return l+k

arr = [2,3,4,7,11]
k = 5
print(kthMissingNumber(arr,k))