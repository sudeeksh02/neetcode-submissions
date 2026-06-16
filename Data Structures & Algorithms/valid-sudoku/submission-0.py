class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=len(board)
        col=len(board[0])
        for i in range(row):
            output=[]
            for j in range(col):
                if board[i][j]=='.':
                    pass
                else:
                    if int(board[i][j])>9:
                        return False
                    if board[i][j] not in output:
                        output.append(board[i][j])
                    else:
                        return False
            
        for i in range(col):
            output=[]
            for j in range(row):
                if board[j][i]=='.':
                    pass
                else:
                
                    if board[j][i] not in output:
                        output.append(board[j][i])
                    else:
                        return False  
        
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):

                output=[]
                for i in range(box_row,box_row+3):
                    for j in range(box_col,box_col+3):
                        if board[i][j]!='.':
                            if board[i][j] in output:
                                return False
                            output.append(board[i][j])
        return True


        


                

        