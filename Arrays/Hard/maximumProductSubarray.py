def maxProduct(nums):
    minProd = nums[0]
    maxProd = nums[0]
    res = nums[0]
    for i in nums[1:]:
        if i<0:
            minProd,maxProd = maxProd, minProd
        
        minProd = min(i,minProd*i)
        maxProd = max(i,maxProd*i)
        res = max(res,maxProd)
    return res

nums = [1, 2, -3, 0, -4, -5]
print(maxProduct(nums))