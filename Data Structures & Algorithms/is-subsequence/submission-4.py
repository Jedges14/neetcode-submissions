class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)+1
        m = len(t)+1
        c = [[0]*n for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                if t[i-1] == s[j-1]:
                    c[i][j] = c[i-1][j-1] + 1

                else:
                    c[i][j] = c[i-1][j]


        return c[m-1][n-1] == len(s)