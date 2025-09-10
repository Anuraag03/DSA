def longestConsecutiveSequence(nums): #TC = O(N) and SC = O(N)
    seen = set(nums)
    maxCount = 0
    for i in nums:
   
        if i-1 not in seen:
            count = 0
            while i in seen:
                count+=1
                i+=1
            maxCount = max(maxCount,count)
    return maxCount

            
print(longestConsecutiveSequence([100, 200, 1, 2, 3, 4]))
