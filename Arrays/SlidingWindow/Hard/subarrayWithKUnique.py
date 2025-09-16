'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
'''
def subarraysWithKDistinct(nums, k):
    def atMost(num):
        if num<0:
            return 0
        seen = {}
        l = 0
        count = 0
        for r in range(len(nums)):
            seen[nums[r]] = seen.get(nums[r],0)+1
            while len(seen)>num:
                seen[nums[l]]-=1
                if seen[nums[l]]==0:
                    del seen[nums[l]]
                l+=1
            count+=r-l+1
        return count
    return atMost(k)-atMost(k-1)
nums = [1,2,1,2,3]
k = 2
print(subarraysWithKDistinct(nums,k))