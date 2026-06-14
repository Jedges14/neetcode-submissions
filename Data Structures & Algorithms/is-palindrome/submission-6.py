class Solution:
    def isPalindrome(self, s: str) -> bool:
        l =0
        r = len(s)-1

        while l<r:
            while  l<r and not self.isal(s[l]):
                l+=1

            while  l<r and not self.isal(s[r]):
                r-=1

            if s[l].lower() != s[r].lower():
                return False

            r-=1
            l+=1

        return True

    def isal(self, c: str):
        return c.isalnum()