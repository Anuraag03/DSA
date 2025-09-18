def nextGreaterII(nums):
    n = len(nums)
    res = [-1]*n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]]>nums[i]:
            res[stack.pop()] = nums[i]
        if i<n:
            stack.append(i)
    return res
nums = [1,2,3,4,3]
print(nextGreaterII(nums))