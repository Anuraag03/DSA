'''
Given Array of Integers find arr[i] and arr[j] such that i<j and arr[i]>arr[j]
'''
def countInversions(nums):
    def merge(nums, low, mid, high):
        temp = []
        l = low
        r = mid + 1
        cnt = 0
        
        while l <= mid and r <= high:
            if nums[l] <= nums[r]:
                temp.append(nums[l])
                l += 1
            else:
                temp.append(nums[r])
                cnt += (mid - l + 1)  # all remaining left elements form inversions
                r += 1
        
        # add leftovers
        while l <= mid:
            temp.append(nums[l])
            l += 1
        while r <= high:
            temp.append(nums[r])
            r += 1
        
        # copy back to original array
        for i in range(low, high + 1):
            nums[i] = temp[i - low]
        
        return cnt

    def mergeSort(nums, low, high):
        cnt = 0
        if low >= high:
            return cnt
        mid = (low + high) // 2
        cnt += mergeSort(nums, low, mid)
        cnt += mergeSort(nums, mid + 1, high)
        cnt += merge(nums, low, mid, high)
        return cnt

    return mergeSort(nums, 0, len(nums) - 1)

    
nums = [3,1,2,6,5]
print(countInversions(nums))
        
