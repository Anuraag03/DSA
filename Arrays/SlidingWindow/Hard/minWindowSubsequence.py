'''
You said:
Given two strings s1 and s2, find the smallest contiguous substring of s1 in which s2 appears as a subsequence.

The characters of s2 must appear in the same order within the substring, but not necessarily consecutively.
If multiple substrings of the same minimum length satisfy the condition, return the one that appears earliest in s1.
If no such substring exists, return an empty string.
Both s1 and s2 consist only of lowercase English letters.
'''
def minWindow(s1, s2): #TC: O(m*n) SC: O(1)
    m, n = len(s1), len(s2)
    min_len = float('inf')
    start_index = -1
    i = 0
    while i < m:
        j = 0
        # forward scan → try to match s2 inside s1
        while i < m:
            if s1[i] == s2[j]:
                j += 1
                if j == n:  # matched full s2
                    break
            i += 1
        if j < n:  # didn’t find full subsequence
            break
        # backward scan → shrink window
        end = i
        j -= 1
        while j >= 0:
            if s1[i] == s2[j]:
                j -= 1
            i -= 1
        i += 1  # move to start of this valid window
        # update answer if this window is smaller
        if end - i + 1 < min_len:
            min_len = end - i + 1
            start_index = i
        # move forward to search next window
        i = i + 1
    return "" if start_index == -1 else s1[start_index:start_index + min_len]

s1 = "geeksforgeeks"
s2 = "eksrg"
print(minWindow(s1,s2))