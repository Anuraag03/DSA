'''
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, 
divide all the array by it, and sum the division's result. 
Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
Each result of the division is rounded to the nearest integer greater than or equal to that element. 
(For example: 7/3 = 3 and 10/2 = 5).
The test cases are generated so that there will be an answer.
'''

def smallestDivisorforThreshold(nums,threshold):
    if threshold<len(nums):
        return -1
    def meetsThreshold(num):
        currsum = 0
        for i in nums:
            currsum+= (i+num-1)//num
        return currsum <=threshold

    l = 1 
    h = max(nums)
    ans = h
    while l<=h:
        mid = (l+h)//2
        if meetsThreshold(mid):
            ans = mid
            h = mid-1
        else:
            l = mid+1
    return ans

nums = [1,2,5,9]
threshold = 6
print(smallestDivisorforThreshold(nums,threshold))