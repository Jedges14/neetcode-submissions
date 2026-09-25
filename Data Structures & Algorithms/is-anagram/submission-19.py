class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = [0]*26

        if len(s)!=len(t): return False

        s = s.lower()
        t = t.lower()


        for n in range(len(s)):
            res[ord(s[n])-ord('a')]+=1
            res[ord(t[n])-ord('a')]-=1

        for i in res:
            if i!=0:
                return False
            
        return True