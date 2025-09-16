'''
A digit string is good if the digits (0-indexed) at even 
indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at 
even positions are even and the digits (5 and 2) at odd positions are prime.
 However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. 
Since the answer may be large, return it modulo 10^9 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
'''
def goodNumbers(num):
    MOD = 10**9 + 7
    def power(x,n):
        if n == 0:
            return 1
        half = power(x,n//2)
        if n%2==1:
            return half*half*x%MOD
        else:
            return half*half%MOD
    even = (num+1)//2
    odd = num//2
    return power(5,even)*power(4,odd)

print(goodNumbers(4))