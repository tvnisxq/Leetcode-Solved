class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initializing two pointers
        l, r = 0, len(height) - 1
        # To keep track of the maximum area that we can get
        max_area = 0

        # This loop traverses until left and right pointers merge 
        # at a common points and hence area can't be calculated using 
        # single height
        while l < r:
            width = r - l
            curr_height = min(height[l], height[r]) # taking the minimum of the left & right heights
            area = width * curr_height  # calculating area using length*width
            max_area = max(max_area, area)  # opting max_area to whatever(max_area or area) the maximum comes to be

            # Now if the height[l] is less than height[r], we move 'l' pointer towards 
            # the more heighted bars in order to get the maximum area
            if height[l] < height[r]:
                l += 1      # So we increment the left pointer 
            else:
                r -= 1      # and decrement the right pointer otherwise
        
        return max_area
            
            