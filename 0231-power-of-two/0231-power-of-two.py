class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Basic Implementation:
        """
        power = 1
        count = 1

        while power <= n:
            if power == n:
                return True
            power = 2 ** count
            count += 1
        return False
