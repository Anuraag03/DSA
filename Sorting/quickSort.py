def quickSort(nums,low,high): #TC= O(NlogN) or O(N^2) if bad pivot is picked and SC = O(N) recursive stack space
    if low>=high:
        return
    pi = partition(nums,low,high)
    quickSort(nums,low,pi-1)
    quickSort(nums,pi+1,high)

def partition(nums,low,high):
    pivot = nums[high]
    i = low
    for j in range(low,high):
        if nums[j]<pivot:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
    nums[i],nums[high] = nums[high],nums[i]
    return i

nums = [5,2,1,3,4,6]
quickSort(nums,0,len(nums)-1)
print(nums)  