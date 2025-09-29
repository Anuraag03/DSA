def countSubarraysWithXor(nums,k):
    xor = 0
    prefix = {0:1}
    count = 0
    for i in range(len(nums)):
        xor^=nums[i]
        if xor^k in prefix:
            count+=prefix[xor^k]
        prefix[xor] = prefix.get(xor,0)+1
    return count


nums = [4, 2, 2, 6, 4]
k = 6
print(countSubarraysWithXor(nums, k))  