# class Solution:
    # def solveSudoku(self, board: List[List[str]]) -> None:
    #     """
    #     Main function that modifies the board in place to solve sudoku.
    #     TIME: Worst case -> O(9^n); n = number of empty cells.
    #     SPACE: O(1) -> Only using the board itself, recursion stack depth is atmost 81.
    #     """
    #     self.solve(board)
    
    # def solve(self, board):
    #     """
    #     Recursive Backtracking function:
    #     returns Ture if puzzle is solved, False if current path is invalid.
    #     """
    #     # Step 1: Find the next empty cell:
    #     for row in range(9):
    #         for col in range(9):
    #             if board[row][col] == '.':
    #                 # Step 2: Try each number 1-9 in this empty cell.
    #                 for num in '123456789':
    #                     # Step 3: Check if this number is valid in current position
    #                     if self.isValid(board, row, col, num):
    #                         # Step 4: Place the number -> make a choice.
    #                         board[row][col] = num
    #                         # Step 5: Recursively solve the rest of the puzzle
    #                         if self.solve(board):
    #                             return True # Found a solution
    #                         # Step 6: Backtrack -> this number didn't work
    #                         # Remove it & try the next number.
    #                         board[row][col] = '.'
    #                 # Step 7: If no number 1-9 works in this cell,
    #                 # this path is invalid, return False to backtrack
    #                 return False
    #     # Step 8: If we've filled all cells successfully, puzzle is solved.
    #     return True

    # def isValid(self, board, row, col, num):
    #     """
    #     Check if placing num at board[row][col] violates any sudoklu rules.
    #     Returns True if valid & False otherwise. 
    #     """
    #     # Check 1: Row Constraint -> is num already in this row?
    #     for j in range(9):
    #         if board[row][j] == num:
    #             return False
        
    #     # Check 2: Column Constraint -> is num already in this column?
    #     for i in range(9):
    #         if board[i][col] == num:
    #             return False
        
    #     # Check 3: 3x3 Box Constraint -> is num already in this 3x3 box?
    #     # Find the top-left corner of the 3x3 box containing containing rwo, col.
    #     box_row = 3 * (row // 3) # 0, 3, 6
    #     box_col = 3 * (col // 3) # 0, 3, 6

    #     # Check all 9 cells in this 3x3 box.
    #     for i in range(box_row, box_row+3):
    #         for j in range(box_col, box_col+3):
    #             if board[i][j] == num:
    #                 return False
    #     # If all three constraints are satisfied, the placement is valid.
    #     return True

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Set Based Optimization with clear Progression.
        TIME: O(9^k) -> k is the number of empty cell but with siginificant pruning.
        SPACE: O(1) -> Auxiliary space, constraint sets are fixes size

        Key optimizations:
        • Pre-compute empty cells(avoid repeated board scanning).
        • Use sets for O(1) constraint checking.
        • Early termination & efficient backtracking.
        """
        # Step 1: Initialize Constraint tracking sets.
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

        # Step 2: Populate Constraint sets and find empty cells.
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i,j))
                else:
                    num = board[i][j]
                    self.rows[i].add(num)
                    self.cols[j].add(num)
                    self.boxes[self.getBoxIndex(i, j)].add(num)
        self.backTrack(board, empty_cells, 0)
        
    # Step 3: Solve using optimized Backtracking
    def backTrack(self, board, empty_cells, index):
        """
        Core Backtracking with O(1) constraint checking.
        """
        # Base Case: all empty cells filled.
        if index == len(empty_cells):
            return True
        row,col = empty_cells[index]
        box_idx = self.getBoxIndex(row, col)

        # Try each digit 1-9.
        for num in '123456789':
            # O(1) constraint validation using sets
            if (num not in self.rows[row] and
                num not in self.cols[col] and
                num not in self.boxes[box_idx]):

                # Make the move: Place number and update constraints
                self.placeNumber(board, row, col, num, box_idx)
                
                # Recursive call to fit next empty cell
                if self.backTrack(board, empty_cells, index + 1):
                    return True

                # Backtrack: remove number and revert constraints
                self.removeNumber(board, row, col, num, box_idx)
            
        # No valid number found for this cell
        return False

    def placeNumber(self, board, row, col, num, box_idx):
        """ Helper: place number & update all constraint sets"""
        board[row][col] = num
        self.rows[row].add(num)
        self.cols[col].add(num)
        self.boxes[box_idx].add(num)

    def removeNumber(self, board, row, col, num, box_idx):
        """ Helper: Remove number & remove all constraint sets"""
        board[row][col] = '.'
        self.rows[row].remove(num)
        self.cols[col].remove(num)
        self.boxes[box_idx].remove(num)
    
    def getBoxIndex(self, row, col):    
        """
        Convert (row, col) coordinates to
        box index (0-8)
        Box arrangement:
        [0][1][2]
        [3][4][5]
        [6][7][8]
        """
        return (row//3) * 3 + col // 3