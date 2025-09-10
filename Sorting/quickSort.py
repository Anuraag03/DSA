def quickSort(nums,low,high): #TC= O(NlogN) or O(N^2) if bad pivot is picked and SC = O(N) recursive stack space
    if low>=high:
        return
    pi = partition(nums,low,high)
    quickSort(nums,low,pi-1)
    quickSort(nums,pi+1,high)

def partition(nums,low,high):
    pivot = nums[high]
    i = low-1
    for j in range(low,high):
        if nums[j]<pivot:
            i+=1
            nums[i],nums[j] = nums[j],nums[i]
    nums[i+1],nums[high] = nums[high],nums[i+1]
    return i+1
