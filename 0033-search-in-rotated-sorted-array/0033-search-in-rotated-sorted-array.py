class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # First BS(traditional) to find the minimum element
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        
        min_index = right

        # Setting up the range for another BS which is going to check
        # if the minimum element is the target element
        if min_index == 0:
            left, right = 0, n - 1
        elif nums[0] <= target <= nums[min_index - 1]:
            left, right = 0, min_index - 1
        else:
            left, right = min_index, n - 1
        
        # Second BS
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
                
        return -1