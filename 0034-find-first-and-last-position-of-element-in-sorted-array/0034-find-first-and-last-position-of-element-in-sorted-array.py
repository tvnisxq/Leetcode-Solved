class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.binarySearch(nums, target, True)
        r = self.binarySearch(nums, target, False)
        return [l, r]
        
        
    def binarySearch(self, nums, target, leftBias):
        left, right = 0, len(nums) - 1
        i = -1

        while left <= right:

            middle = (left + right) // 2
            if target > nums[middle]:
                left = middle + 1
            
            elif target < nums[middle]:
                right = middle - 1
            
            else:
                i = middle
                if leftBias:
                    right = middle - 1
                else:
                    left = middle + 1
        
        return i