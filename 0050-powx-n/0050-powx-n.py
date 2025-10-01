class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
        # Handling the edge cases
            if x == 0: return 0 
            if n == 0: return 1 
            
            # Core Logic for recursion
            res = helper(x, n // 2)
            res = res * res
            
            # If n is odd multiply by x once more
            return x * res if n % 2 else res  

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res