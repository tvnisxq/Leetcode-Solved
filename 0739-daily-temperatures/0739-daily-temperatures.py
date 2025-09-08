class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ Daily Temperatures"""
        # Time: O(n)
        # Space: O(n)
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i
            
            stack.append((t, i))
        return res