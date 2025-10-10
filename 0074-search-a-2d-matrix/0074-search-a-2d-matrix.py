class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n 
        l, r = 0, t - 1

        while l <= r:
            mid = (l+r) // 2
            i, j = mid // n, mid % n
            mid_num = matrix[i][j]

            if mid_num == target:
                return True 
            elif mid_num < target:
                l = mid + 1
            else:
                 r = mid - 1
        
        return False


            


