class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        c = [[0]* i for i in range(1, rowIndex+2)]

        for i in range(len(c)):
            c[i][0] = 1
            c[i][-1] = 1


        for i in range(1,len(c)):
            for j in range(1, len(c[i])-1):
                c[i][j] = c[i-1][j-1] + c[i-1][j]


        return c[len(c)-1]