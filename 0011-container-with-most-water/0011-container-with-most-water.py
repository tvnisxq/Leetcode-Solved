class Solution:
    def maxArea(self, height: List[int]) -> int:

        # initializing the pointers
        l, r = 0, len(height) - 1 
        # creating a variable to store max_area
        max_a = 0

        # loop traverses until left & right pointers merge at a common point,
        # and hence area can't be calculated using a single height
        while l < r:

            w = r - l 
            h = min(height[l], height[r]) # taking the minimum of the heights at left & right
            a = w * h # calculating area using (Length*Breadth)
            max_a = max(max_a, a) # opting max_area to whatever(max_are or area) the maximum comes to be.

            # if height of left is less than height of right,
            # so we need to increase the height of l to move towards maximum area
            if height[l] < height[r]:
                l += 1 # so we increment the left pointer
            else:
                r -= 1
       # After the loop finishes return the maximum area found.
        return max_a