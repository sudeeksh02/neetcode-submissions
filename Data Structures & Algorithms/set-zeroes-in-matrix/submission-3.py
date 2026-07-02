class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #check for rows
        m=len(matrix)
        n=len(matrix[0])

        row,col=0,0
        for i in range(n):
            if matrix[0][i]==0:
                row=1
        for j in range(m):
            if matrix[j][0]==0:
                col=1


        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0],matrix[0][j]=0,0

        for i in range(1,n):
            if matrix[0][i]==0:
                j=0
                while j<m:
                    matrix[j][i]=0
                    j+=1
        for i in range(1,m):
            if matrix[i][0]==0:
                j=0
                while j<n:
                    matrix[i][j]=0
                    j+=1
        if row:
            for i in range(n):
                matrix[0][i]=0
        if col:
            for i in range(m):
                matrix[i][0]=0

        