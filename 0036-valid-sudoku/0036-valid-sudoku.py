# # Verbose method:
# '''
# DEMERITS:
# • Slower loop wise: loops the board 
# thrice(though still O(1) in practice since the board is 9x9)

# • Slight redundancy: repeats the same logic thrice with minor 
# changes


# MERITS:
# • Easy to understand: Each loop does only 1 job
# • Beginner friendly.
# • Easy to isolate and debug one specific case(row,column, or box) 
# '''
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         #  Validate Rows
#         for i in range(9):
#             s= set()
#             for j in range(9):
#                 item = board[i][j]
#                 if item in s:
#                     return False
#                 elif item !='.':
#                     s.add(item)

#         #  Validate Columns:
#         for i in range(9):
#             s= set()
#             for j in range(9):
#                 item = board[j][i]
#                 if item in s:
#                     return False
#                 elif item !='.':
#                     s.add(item)

#         # Validate 3x3 boxes:
#         starts = [(0, 0), (0, 3), (0, 6),
#                   (3, 0), (3, 3), (3, 6),
#                   (6, 0), (6, 3), (6, 6)]

#         for i,j in starts:
#             s= set()
#             for row in range(i, i+3):
#                 for col in range(j, j+3):
#                     item =  board[row][col]
#                     if item in s:
#                         return False
#                     elif item != '.':
#                         s.add(item)
#         return True

# Optimal Method:
'''
• Only 1 pass over the board: Faster in terms of code execution and cache performance.
• Little-to- None Redundancy: No repeated logic, clean code.
• Interview Friendly: Smart and clever approach
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool :
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        #Check every cell in the board:
        for i in range(9):
            for j in range(9):
                val = board[i][j]

                #Skip empty cells as they're not violating any rules:
                if val == '.':
                    continue
                
                # Calculate box index:
                box_index = (i // 3) *3 + (j // 3)

                # Check if the value we are processing already exists in another row,col, or boxes:
                if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                    return False

                '''
                Add the value in the set if it doesn't exist already:
                helps to keep track of the elements we've seen til now. 
                '''
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)

        # Having Checked all the cells and no rules are broken: Valid Sudoku
        return True