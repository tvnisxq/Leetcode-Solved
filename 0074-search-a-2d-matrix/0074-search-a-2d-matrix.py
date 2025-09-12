class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # store number of rows in m
        n = len(matrix[0]) # store number of columns in n
        t = m * n # total number of cells in the matrix
        
        # Declare two pointers
        left = 0
        right = t - 1

        while left <= right:
            middle = (left + right) // 2
            """
            Calculating the 'i' & 'j' index(in terms of matrix)
            """
            i = middle // n 
            j = middle % n
            mid_num = matrix[i][j]
            
            if target == mid_num:
                return True

            elif target < mid_num:
                right = middle - 1
            
            else:
                left = middle + 1
        
        return False