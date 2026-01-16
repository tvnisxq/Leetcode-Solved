# MEMOIZATION Approach
# Time: O(n) -> Each num is calculated once
# Space: O(n) -> for the cache and the recursion stack
class Solution:
    def fib(self, n: int) -> int:
        # Create a cache to store computed results
        memo ={}

        def helper(num):
            # Base Cases
            if num == 0: return 0
            if num == 1: return 1

            # Check if we've already calculated this
            if num in memo:
                return memo[num]

            # Calcuate and store in cache
            memo[num] = helper(num-1) + helper(num-2)
            return memo[num]

        return helper(n)