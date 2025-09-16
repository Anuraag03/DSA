def longestKSubstr(s, k):
    seen = {}
    l = 0
    maxLen = -1
    
    
    for r in range(len(s)):
        seen[s[r]] = seen.get(s[r],0)+1
        while len(seen)>k:
            seen[s[l]]-=1
            if seen[s[l]] == 0:
                del seen[s[l]]
            l+=1
        if len(seen)==k:
            maxLen = max(maxLen,r-l+1)
    return maxLen

s = "aabacbebebe"
k = 3
print(longestKSubstr(s,k))