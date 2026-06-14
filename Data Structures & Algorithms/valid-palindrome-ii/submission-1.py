class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1: return True

        if self.isPal(s): return True

        res = []
        for i in range(len(s)):
            l = s[:i] + s[i+1:]
            res.append(self.isPal(l))

        print(res)


        if True in res:
            return True
        else:
            return False


    def isPal(self, w) :

        l =0
        r = len(w) -1

        while l<r:
            if w[l] != w[r]: 
                return False

            r-=1
            l+=1

        return True