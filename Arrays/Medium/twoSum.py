def twoSumValues(nums, k): #TC = O(NlogN) and SC = O(1)
    nums.sort()
    l, r = 0, len(nums) - 1
    res = []
    
    while l < r:
        total = nums[l] + nums[r]
        
        if total == k:
            res.append((nums[l], nums[r]))
            
            # skip duplicates for left
            left_val = nums[l]
            while l < r and nums[l] == left_val:
                l += 1
            
            # skip duplicates for right
            right_val = nums[r]
            while l < r and nums[r] == right_val:
                r -= 1
        
        elif total < k:
            l += 1
        else:
            r -= 1
    
    return res

        
def twoSumValues_set(nums, k): #TC = O(N) and SC = O(N)
    seen = set()
    res = set()
    
    for num in nums:
        target = k - num
        if target in seen:
            res.add((min(num, target), max(num, target)))
        seen.add(num)
    
    return list(res)

arr = [2, 6, 5, 8, 11]
target = 14
print(twoSumValues_set(arr,target))
print(twoSumValues(arr,target))
