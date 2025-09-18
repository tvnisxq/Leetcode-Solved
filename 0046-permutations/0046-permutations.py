class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # Base Case
        if (len(nums) == 1):
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            # recursive call
            pers = self.permute(nums)

            for per in pers:
                per.append(n)
            result.extend(pers)
            nums.append(n)

        return result