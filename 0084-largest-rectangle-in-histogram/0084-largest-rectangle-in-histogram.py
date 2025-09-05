class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)    
        stack = []
        max_a = 0
        
        for i, height in enumerate(heights):
            # Monotonic Stack
            start = i
            while stack and height < stack[-1][0]:
                h, j  = stack.pop()
                w = i-j
                a = h*w 
                max_a = max(max_a, a)
                start = j
            stack.append((height, start))

        while stack:
            h, j = stack.pop()
            w = n - j
            max_a = max(max_a, h*w)
        
        return max_a