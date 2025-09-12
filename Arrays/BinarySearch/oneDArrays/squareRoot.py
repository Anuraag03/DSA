def findSquareRoot(num):
    l = 1
    h = num
    ans = -1
    while l<=h:
        mid = (l+h)//2
        if mid*mid<=num:
            ans = mid
            l = mid+1
        else:
            h = mid-1
    return ans

print(findSquareRoot(5))
print(findSquareRoot(4))
