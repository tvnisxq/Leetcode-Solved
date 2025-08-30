class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
            Brute Force Solution:
        '''
        # Iterate over each row & column of the 9x9 board:
        for i in range(9): # for each row 
            for j in range(9): # for each column
                if board[i][j] == '.': # if the cell is empty
                    # continue because we need to validate only the filled cells
                    continue 
                          
                # Logic for checking Rows:
                for row in range(9):
                    # We want to check in every other cell if the
                    # val at current cell is equal to val at any of the 
                    # other cells
                    if row != i and board[row][j] == board[i][j]: 
                        return False
            
                #  Logic for checking Cols:
                for col in range(9):
                    if col != j and board[i][col] == board[i][j]:
                        return False

                # Logic for checking the 3x3 boxes:
                start_row = 3 * (i//3)
                start_col = 3 * (j//3)

                # We want to consider every other cell except the cell that we're in
                # if we want to check the other cell whether they're having the same val
                # as our current cell 
                for x in range(start_row, start_row + 3):
                    for y in range(start_col, start_col + 3):
                        if (x != i or y != j) and board[x][y] == board[i][j]:
                            return False
        return True
                
