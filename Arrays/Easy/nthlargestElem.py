import heapq
def nthLargest(nums,n):
    # you can use sorting and solve in O(nlogn) or use the below heap method
    heap = [] # TC= O(Nlogn) N = size of array, n = the nth value we want to find
    for i in nums:
        heapq.heappush(heap,i)
        if len(heap)>n:
            heapq.heappop(heap)
    return heap[0]
            
def quickSelect(nums,n): #quickselect algorithm for nth largest element TC = O(N) avg case
    k = len(nums)-n
    def select(nums,low,high):
        pivot = nums[high]
        i = low
        for j in range(low,high):
            if nums[j]<pivot:
                nums[j],nums[i] = nums[i],nums[j]
                i+=1
        nums[i],nums[high] = nums[high],nums[i]
        if i==k:
            return nums[i]
        elif i<k:
            return select(nums,i+1,high)
        else:
            return select(nums,low,i-1)
    return select(nums,0,len(nums)-1)

n = 3
nums = [1,4,2,5,7,3,6]
print(nthLargest(nums,n))
print(quickSelect(nums,n))


