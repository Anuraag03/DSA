def binarySubarraysWithSumK(nums,k): #using hashMap TC:O(n) SC:O(n)
    prefixSum = {}
    prefixSum[0] = 1
    currSum = 0
    count = 0
    for i in range(len(nums)):
        currSum+=nums[i]
        if currSum-k in prefixSum:
            count+=prefixSum[currSum-k]
        prefixSum[currSum] = prefixSum.get(currSum,0)+1
    return count

def binarySubarraysWithSumKSlidingWindow(nums,k): 
    #using sliding window
    # we are calculation number of subarrays with sum<=k and subtracting of
    # subarrays with sum<=k-1 from the above 
    # TC:O(n) SC:O(1)
    def atMost(num):
        if num<0:
            return 0
        l = 0
        count = 0
        currSum = 0
        for r in range(len(nums)):
            currSum+=nums[r]
            while currSum>num:
                currSum-=nums[l]
                l+=1
            count+=r-l+1
        return count
    return atMost(k)-atMost(k-1)

nums = [1,0,1,0,1]
goal = 2
print(binarySubarraysWithSumK(nums,goal))
print(binarySubarraysWithSumKSlidingWindow(nums,goal))



