import heapq
def subsetSum(nums):
    res = []
    def rec(n,total):
        if n == len(nums):
            res.append(total)
            return
        rec(n+1,total+nums[n])
        rec(n+1,total)
    rec(0,0)
    return sorted(res)

nums = [1,2,5]
print(subsetSum(nums))

