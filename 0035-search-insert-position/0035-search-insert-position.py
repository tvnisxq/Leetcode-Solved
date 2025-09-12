class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """ Basic Binary Search"""
        n = len(nums)
        left = 0 
        right = n - 1

        while left <= right:
            middle = (left+right) // 2
            
            if nums[middle] < target:
                left = middle + 1
                
            elif nums[middle] > target:
                right = middle - 1
            
            else:
                return middle
        
        if nums[middle] < target:
            return middle + 1
        else:
            return middle