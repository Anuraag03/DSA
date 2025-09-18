'''
The next greater element of some element x in an array 
is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2,
where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] 
and determine the next greater element of nums2[j] in nums2. If there is no next greater element, 
then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
'''
def nextGreaterI(nums1,nums2):
    nextGreater = {}
    stack = []
    for i in nums2:
        while stack and stack[-1]<i:
            nextGreater[stack.pop()] = i
        stack.append(i)
    while stack:
        nextGreater[stack.pop()] = -1
    return [nextGreater[num] for num in nums1]

print(nextGreaterI([4,1,2],[1,4,2,3]))
