class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        '''
        we only need to count the number of (x,y)
        pairs whose sum, x+y is odd. And in all possible 
        pairs of (x,y), only half of them would be odd, 
        which is handled via floor division by 2.
        '''
        return (n*m) // 2
