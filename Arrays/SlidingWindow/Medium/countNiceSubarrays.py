'''
Given an array of integers nums and an integer k. 
A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.
'''
def countNiceArrays(nums,k):
    def atMost(num):
        if num<0:
            return 0
        l = 0
        currNum = 0
        count = 0
        for r in range(len(nums)):
            currNum += nums[r]%2
            while currNum>num:
                currNum-=nums[l]%2
                l+=1
            count+=r-l+1
        return count
    return atMost(k)-atMost(k-1)

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(countNiceArrays(nums,k))

            