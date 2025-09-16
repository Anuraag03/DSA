def genBinaryStrings(num): #TC: O(2^n x n) Sc : O(n x 2^n)
    res = [] 
    def rec(n,str):
        if n == num:
            res.append(str)
            return
        rec(n+1,str+'0')
        rec(n+1,str+'1')
    rec(0,'')
    return res

def genBinaryStringsWithoutAdjacentOnes(num):
    res = []
    def rec(n,str):
        if n == num:
            res.append(str)
            return
        rec(n+1,str+'0')
        if not str or str[-1]!='1':
            rec(n+1,str+'1')
    rec(0,'')
    return res
print(genBinaryStrings(3))
print(genBinaryStringsWithoutAdjacentOnes(3))