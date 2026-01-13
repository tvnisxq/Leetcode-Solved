class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        t = rows * cols
        l, r = 0, t-1

        while l <= r:
            m = (l+r) // 2
            i = m // cols
            j = m % cols
            mid_num = matrix[i][j]

            if mid_num == target:
                return True
            elif mid_num < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
