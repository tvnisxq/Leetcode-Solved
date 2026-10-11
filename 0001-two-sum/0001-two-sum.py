class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i