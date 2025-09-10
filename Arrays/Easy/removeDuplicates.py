def removeDuplicatesInSortedArrays(nums): #TC = O(N) and SC = O(1)
    pointer = 1
    for i in range(1,len(nums)):
        if nums[i]!=nums[pointer-1]:
            nums[pointer],nums[i] = nums[i],nums[pointer]
            pointer += 1
    return nums[:pointer]

def removeDuplicates(nums):# TC = O(N) and SC = O(N)
    pointer = 0
    seen = set()
    for i in nums:
        if i not in seen:
            seen.add(i)
            nums[pointer] = i
            pointer+=1
    return nums[:pointer]

nums = [1,1,2,3,4,4]
nums2 = [1,5,2,6,1,2,3,5,7]
print(removeDuplicatesInSortedArrays(nums))
print(removeDuplicates(nums2))