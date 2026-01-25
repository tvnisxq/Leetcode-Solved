class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x = -x if neg else x
        rev = 0
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        if neg:
            rev = -rev
        return rev if -2**31 <= rev <= 2**31 -1 else 0
        