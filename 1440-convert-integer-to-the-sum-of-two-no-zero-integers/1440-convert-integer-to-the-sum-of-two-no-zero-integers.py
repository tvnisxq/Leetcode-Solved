class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """ 
        Most Intuitive Solution 
        Time: O(n²)
        Space: O(n) 
        """
        
        # valid = []
        # for i in range(n):
        #     if not '0' in str(i):
        #         valid.append(i)
        
        # for x in valid:
        #     for y in valid:
        #         if x+y == n: return [x, y]
        
        """
        Eficient Solution:
        Time: O(n logn)
        Space: O(1)
        """
        # Given a+b = n; b = n-a
        for a in range(1, n):
            b = n - a
            if not '0' in str(a) and not '0' in str(b):
                return [a, b]

