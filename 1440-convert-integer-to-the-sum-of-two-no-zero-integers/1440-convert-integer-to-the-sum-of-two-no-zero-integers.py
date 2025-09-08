class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """ 
        Most Intuitive Solution 
        Time: O(n²)
        Space: O(n) 
        """
        
        valid = []
        for i in range(n):
            if not '0' in str(i):
                valid.append(i)
        
        for x in valid:
            for y in valid:
                if x+y == n: return [x, y]
        
        """
        Eficient Solution:
        Time: O(n)
        Space: O()
        """

        