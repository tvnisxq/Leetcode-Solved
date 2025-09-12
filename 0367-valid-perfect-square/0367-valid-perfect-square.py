class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """ Brute Force: TLE"""
        # for x in range(1, num+1):
        #     if x ** 2 == num:
        #         return True
        # return False

        """ Binary Search Solution"""
        # Time: O(log n); binary search, repetitive shortening of search range
        # Space: O(1); we're not storing anything except a few vaiables
        left = 1
        right = num

        while left <= right:
            middle = (left + right) // 2
            m_squared = middle * middle

            if num == m_squared:
                return True
            
            elif num < m_squared:
                right = middle - 1
            
            else:
                left = middle + 1
        
        return False
