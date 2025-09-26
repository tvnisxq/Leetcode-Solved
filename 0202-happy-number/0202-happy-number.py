class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = str(n)

        while cur not in seen:
            seen.add(cur)
            sum = 0

            for digit in cur:
                digit = int(digit)
                sum += digit ** 2 
            
            if sum == 1: return True
            cur = str(sum)

        return False
