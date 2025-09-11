'''
Merge Two Arrays of size n and m 
without using extra space, such that they are sorted 
and first array contains first n elements and 
second array contains next n elements
'''
def mergingTwoArrays(nums1,nums2):
    n = len(nums1)
    m = len(nums2)
    totLen = n+m
    gap = (totLen//2)+(totLen%2)
    while gap>0:
        left = 0
        right = left+gap
        while right<totLen:
            if left<n and right>=n:
                if nums1[left]>nums2[right-n]:
                    nums1[left],nums2[right-n] = nums2[right-n],nums1[left]
            elif left>=n:
                if nums2[left-n]>nums2[right-n]:
                    nums2[left-n],nums2[right-n] = nums2[right-n],nums2[left-n]
            else:
                if nums1[left]>nums1[right]:
                    nums1[left],nums1[right] = nums1[right],nums1[left]
            left+=1
            right+=1
        
        if gap==1:
            break
        gap = (gap//2)+(gap%2)

nums1 = [1,5,4]
nums2 = [2,6,3]
mergingTwoArrays(nums1,nums2)
print(nums1)
print(nums2)