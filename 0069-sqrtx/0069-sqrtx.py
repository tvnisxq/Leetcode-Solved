class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # Edge Case:
        if x < 2:
            return x
        
        left, right = 1, x

        while left <= right:
            middle = (left + right) // 2
            sqr = middle * middle

            if sqr == x:
                return middle
            
            elif sqr > x:
                right = middle - 1
            
            else:
                left = middle + 1
        
        return right