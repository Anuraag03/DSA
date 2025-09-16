def palindromePartitioning(s):
    def isPalindrome(str):
        l = 0
        r = len(str)-1
        while l<=r:
            if str[l]!=str[r]:
                return False
            l+=1
            r-=1
        return True
    res = []
    def rec(n,ans):
        if n == len(s):
            res.append(ans[:])
            return
        for i in range(n,len(s)):
            currStr = s[n:i+1]
            if isPalindrome(currStr):
                ans.append(currStr)
                rec(i+1,ans)
                ans.pop()
    rec(0,[])
    return res

print(palindromePartitioning('aab'))
