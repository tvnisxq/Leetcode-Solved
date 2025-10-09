class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Edge Case
        if not nums or len(nums) < 2:
            return []
        
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i
        
        return []