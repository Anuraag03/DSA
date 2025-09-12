import math
def minEatingSpeed(piles,h): #TC O(nlog(max(piles)))
    def canEat(num):
        hours = 0
        for p in piles:
            hours+=math.ceil(p/num)
        return hours<=h
    l = 1
    r = max(piles)
    ans = 1
    while l<=r:
        mid = (l+r)//2
        if canEat(mid):
            ans = mid
            r = mid-1
        else:
            l = mid+1
    return ans


print(minEatingSpeed([3,6,7,11],8))
