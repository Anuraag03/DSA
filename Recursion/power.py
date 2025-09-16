def power(x,n): #TC: O(logn) SC: O(logn)
    if n == 0:
        return 1
    half = power(x,n//2)
    if n%2 == 1:
        return half*half*x
    else:
        return half*half
    
print(power(2,5))