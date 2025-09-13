'''
Given a binary array nums, find max consecutive 1's if k 0's  can be flipped to 1 
'''
def maxConsecutiveOnes(nums,k):
    l = 0
    r = 0
    maxLen = 0
    counter = 0
    for r in range(len(nums)):
        if nums[r]==0:
            counter+=1
        if counter>k:
            if nums[l] == 0:
                counter-=1
            l+=1
        maxLen = max(maxLen,r-l+1)
    return maxLen
        
print(maxConsecutiveOnes([1,1,1,0,0,0,1,1,1,1,0],2))