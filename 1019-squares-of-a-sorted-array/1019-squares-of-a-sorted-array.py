class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
            Two Pointers Algorithm:
            ▷ Left pointer is placed at the beginning & the right at the end of the array
            ▷ The left pointer moves to the right, the right pointer moves to the left,
            squeezing the array, until they cross each other.
        '''
        # left pointer at the beginning
        left = 0
        # right pointer at the end
        right = len(nums) - 1
        # empty array to store the result
        result = []

        # The loop runs while the left & right pointer are still
        # not equal or left one is at an index than that of the right pointer.
        while left <= right:
            '''
            Here we take absolute values of the array because it 
            addresses the effect of squaring negative numbers.
            '''
            # if absolute of nums at left is greater than the absolute of nums at right:
            if abs(nums[left]) > abs(nums[right]):
                # square the number and append it to the result
                result.append(nums[left] ** 2)
                # move the left pointer one step ahead
                left += 1
            
            # however if the absolute of nums at right is greater or equal
            # than the absolute of nums at left:
            else:
                # square the number and append it.
                result.append(nums[right] ** 2)
                # move the right pointer ahead by 1 step
                right -= 1

        # Currently the list is sorted in a decreasing order
        # so we reverse it.
        result.reverse()
        
        # then finally return it.
        return result