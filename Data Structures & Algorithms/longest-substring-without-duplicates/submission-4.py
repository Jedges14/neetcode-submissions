class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        se = set()
        le = 0

        while r<len(s):
            while s[r] in se:
                se.remove(s[l])
                l+=1
            se.add(s[r])
            le = max(le, r-l+1)
            r+=1

        return le

        