class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1 = Counter(s) 
        
        for n in range(len(s)):
            s1[t[n]] -= 1

        for v in s1.values():
            if v!=0: return False

        return True
