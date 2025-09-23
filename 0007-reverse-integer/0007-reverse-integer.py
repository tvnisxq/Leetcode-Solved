class Solution:
    def reverse(self, x: int) -> int:
        # Time: O(n)
        # Space: O(1)
        # MIN = -(2 ** 31)
        # MAX = (2 ** 31) - 1

        # res = 0 
        # while x:
        #     digit = int(math.fmod(x, 10)) # -1 % 10 = 9
        #     x = int(x / 10) # -1 // 10 = -1

        #     if (res > MAX // 10 or 
        #         (res == MAX // 10 and digit >= MAX % 10)):
        #         return 0
            
        #     if (res < MIN // 10 or
        #         (res == MIN // 10 and digit <= MIN %10)):
        #         return 0

        #     res = (res * 10) + digit
        
        # return res
            
        neg = x < 0
        x = -x if neg else x
        rev = 0
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        if neg:
            rev = -rev
        return rev if -2**31 <= rev <= 2**31 - 1 else 0

                