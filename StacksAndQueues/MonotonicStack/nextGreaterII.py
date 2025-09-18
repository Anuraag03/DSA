'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]),
return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
'''
def nextGreaterII(nums):
    n = len(nums)
    res = [-1]*n
    stack = []
    for i in range(2*n):
        while stack and nums[stack[-1]]<nums[i%n]:
            res[stack.pop()] = nums[i%n]
        if i<n:
            stack.append(i)
    return res
nums = [1,2,3,4,3]
print(nextGreaterII(nums))