def majorityElem(nums):
    elem = nums[0]
    count = 1
    for i in range(1,len(nums)):
        if nums[i] == elem:
            count+=1
        else:
            count-=1
        if count == 0:
            elem = nums[i]
            count = 1
    return elem

print(majorityElem([3,3,4,2,4,4,2,4,4])) 
print(majorityElem([2,2,1,1,1,2,2]))  


