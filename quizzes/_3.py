"""
    Question: Add two numbers
    Desc: Given a string s, find the length of the longest substring without repeating characters.
    URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    Resource: Runtime: 69 ms Memory Usage: 14 MB
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = {}
        start = 0
        l = 0
        
        for i,c in enumerate(s):
            #print(f'start:{start}, k:{k}, c:{c}, i:{i}, l:{l}')
            if c in k and start<=k[c]:
                #change to new starting point
                start = k[c]+1
            else:
                l = max(l,i-start+1)
            k[c] = i
        return l