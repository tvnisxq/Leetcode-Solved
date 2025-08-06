class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
            Brute Force Approach:
            •
            •
            •
        '''
        # Iterate through each cell in the 9x9 sudoku board.
        for i in range(9):  # For each row 
            for j in range(9):  # For each column
                if board[i][j] == '.':   # Checking for filled cells only
                    continue

                # Logic for Checking Columns:
                for col in range(9):
                    if col != j and board[i][col] == board[i][j]:
                        return False
                
                # Logic for Checking Rows:
                for row in range(9):
                    if row != i and board[row][j] == board[i][j]:
                        return False
                
                # Logic for Checking the 3x3 Boxes:
                start_row = 3*(i//3)
                start_col = 3*(j//3)

                for x in range(start_row, start_row+3):
                    for y in range(start_col, start_col+3):
                        if(x!=i or y!=j) and board[x][y] == board[i][j]:
                            return False
        return True