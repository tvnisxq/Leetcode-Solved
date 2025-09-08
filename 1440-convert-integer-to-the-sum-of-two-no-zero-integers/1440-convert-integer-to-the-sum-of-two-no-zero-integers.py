class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        
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

