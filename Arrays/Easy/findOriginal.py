'''
In an array where each number appears exactly twice except 1 element , find that one element
'''
def findOriginal(nums):
    x = 0
    for i in nums:
        x^=i
    return x

print(findOriginal([1,2,1,2,3,4,4]))
