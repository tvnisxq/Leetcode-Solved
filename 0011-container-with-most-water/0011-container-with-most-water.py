class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
            Two Pointers(Optimal Solution):

            • TIME: O(n) -> loop runs atmost n times where n is the number of
            elements in the height list. 
            • Space: O(1) -> The algorithm uses a constant number of variables, 
            no additional data structures are used.
        '''
        # initializing the pointers
        l, r = 0, len(height) - 1 
        # creating a variable to store max_area
        max_area = 0

        # loop traverses until left & right pointers merge at a common point,
        # and hence area can't be calculated using a single height
        while l < r:

            width = r - l 
            curr_height = min(height[l], height[r]) # taking the minimum of the heights at left & right
            area = width * curr_height # calculating area using (Length*Breadth)
            max_area = max(max_area, area) # opting max_area to whatever(max_are or area) the maximum comes to be.

            # if height of left is less than height of right,
            # so we need to increase the height of l to move towards maximum area
            if height[l] < height[r]:
                l += 1 # so we increment the left pointer
            else:
                r -= 1
       # After the loop finishes return the maximum area found.
        return max_area