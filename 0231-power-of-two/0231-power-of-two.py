class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        power = count = 1
        
        while power <= n:
            if power == n:
                return True
            power = 2 ** count
            count += 1
        
        return False