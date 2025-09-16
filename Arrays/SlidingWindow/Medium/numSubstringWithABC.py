'''
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.
'''
def numSubStringsWithABC(s):
    aPos = -1
    bPos = -1
    cPos = -1
    count = 0
    for i in range(len(s)):
        if s[i] == 'a':
            aPos = i
        elif s[i] == 'b':
            bPos = i
        else:
            cPos = i
        if aPos!=-1 and bPos!=-1 and cPos!=-1:
            count+=min(aPos,bPos,cPos)+1
    return count

s = "abcabc"
print(numSubStringsWithABC(s))
