class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return False
        
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i
