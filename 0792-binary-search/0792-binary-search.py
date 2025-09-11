class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ Basic Binary Search"""
        # Time: O(log n)
        # Space: O(1) 
        n = len(nums)
        left = 0
        right = n - 1
        
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1
    