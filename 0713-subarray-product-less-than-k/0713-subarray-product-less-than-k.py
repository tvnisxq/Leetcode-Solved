class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Initialize product and count
        prod = 1
        count = 0
        # set left pointer at 0
        left = 0

        # Iterate thrrough array with right pointer
        for right in range(len(nums)):
            # multiply current element to product
            prod *= nums[right]    

            # Shrink window while product >= k
            while left <= right and prod >= k:
                prod //= nums[left]
                left += 1
            
            # add all subarrays ending at right 
            count += right - left + 1

        return count