'''
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
'''
def findMissingNumber(nums):
    x = 0
    for i in range(len(nums)+1):
        x^=i
    for i in nums:
        x^=i
    return x

print(findMissingNumber([0,1,2,4,5]))


