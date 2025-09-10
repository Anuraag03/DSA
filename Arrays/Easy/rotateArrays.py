def leftRotate(nums,d):
    d = d%len(nums)
    nums[:d] = reversed(nums[:d])
    nums[d+1:] = reversed(nums[d+1:])
    nums.reverse()

def rightRotate(nums,d):
    n = len(nums)
    d = d%n
    nums[:n-d] = reversed(nums[:n-d])
    nums[n-d+1:] = reversed(nums[n-d+1:])
    nums.reverse()

nums = [1,2,3,4,5]
nums1 = [1,2,3,4,5]
leftRotate(nums,2)
rightRotate(nums1,2)
print(nums)
print(nums1)