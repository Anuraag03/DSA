def longestSubstrWithoutRepeatingChars(st):
    l = 0
    r = 0
    seen = {}
    maxLen = 0
    for r in range(len(st)):
        if st[r] in seen and seen[st[r]]>=l:
            l = seen[st[r]]+1
        seen[st[r]] = r
        maxLen = max(maxLen,r-l+1)
    return maxLen

print(longestSubstrWithoutRepeatingChars('abcabcab'))




