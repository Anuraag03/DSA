'''
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t (including duplicates) 
is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
'''
def minWindow(s, t):
    m = len(s)
    n = len(t)
    if m<n:
        return ""
    need = {}
    for c in t:
        need[c] = need.get(c, 0) + 1
    window = {}
    have, needCount = 0, len(need)
    resLen = float('inf')
    res = (-1,-1)
    l = 0 
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c,0)+1
        if c in need and need[c]==window[c]:
            have+=1
        while have == needCount:
            if r-l+1<resLen:
                res = (l,r)
                resLen = r-l+1
            window[s[l]]-=1
            if s[l] in need and window[s[l]] < need[s[l]]:
                have -= 1
            l+=1
    l,r = res
    return s[l:r+1] if resLen!=float('inf') else ""        

print(minWindow(s = "ADOBECODEBANC", t = "ABC"))