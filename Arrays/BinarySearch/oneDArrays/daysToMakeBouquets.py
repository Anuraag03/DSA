'''
You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden.
If it is impossible to make m bouquets return -1.

'''
def minDays(bloomDays,m,k): # TC = O(Nlog(max(bloomDays)))
    if m*k>len(bloomDays):
        return -1
    def canMake(days):
        count = 0
        flowers = 0
        for i in bloomDays:
            if i<=days:
                flowers+=1
                if flowers == k:
                    count+=1
                    flowers = 0
            else:
                flowers = 0
        return count>=m
    
    
    l = 0
    h = max(bloomDays)
    ans = h
    while l<=h:
        mid = (l+h)//2
        if canMake(mid) :
            ans = mid
            h = mid-1
        else:
            l = mid+1
    return ans

bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(minDays(bloomDay,m,k))