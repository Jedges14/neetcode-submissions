class Solution:
    def generate(self, numRows: int) -> List[List[int]]:


        c = [[0] * i for i in range(1,numRows+1)]

        print(c)

        #hard code base cases
        for i in range(len(c)):
            c[i][0] = 1
            c[i][-1] = 1


        for i in range(2,len(c)):
            for j in range(1,len(c[i])-1):
                c[i][j] = c[i-1][j-1] + c[i-1][j]


        return c

        