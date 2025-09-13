'''
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations. 
'''

def longestRepeatingCharacterReplacement(s,k):
    l = 0
    maxFreq = 0
    maxLen = 0
    count = {}
    for r in range(len(s)):
        count[s[r]] = count.get(s[r],0)+1
        maxFreq = max(maxFreq,count[s[r]])
        while r-l+1-maxFreq>k:
            count[s[l]]-=1
            l+=1
        maxLen = max(maxLen,r-l+1)
    return maxLen

print(longestRepeatingCharacterReplacement(s = "AABABBA", k = 2))

