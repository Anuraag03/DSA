def findRepeatingAndMissing(nums):
    n = len(nums)
    Sn = (n*(n+1))//2
    S2n = (n*(n+1)*(2*n+1))//6
    S,S2 = 0,0
    for i in nums:
        S+=i
        S2+=i*i
    val1 = S-Sn #x-y
    val2 = (S2-S2n)//val1 #x+y
    X = (val1+val2)//2
    Y = X-(val1)
    return X,Y

nums = [1,2,3,3,5]
print(findRepeatingAndMissing(nums))