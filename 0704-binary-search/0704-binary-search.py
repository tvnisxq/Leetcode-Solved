class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            middle = (l + r) // 2

            if nums[middle] == target:
                return middle
            
            elif nums[middle] > target:
                r = middle - 1 
            
            else:
                l = middle + 1
        
        return -1