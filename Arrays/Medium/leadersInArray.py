'''
A leader is an elem that is greater than all elems to its right
'''
def leadersInArray(nums):
    res = []
    maxElem = float('-inf')
    for i in range(len(nums)-1,-1,-1):
        if nums[i]>maxElem:
            res.append(nums[i])
            maxElem = nums[i]
    return res
print(leadersInArray([2,4,1,3,5,6,4]))