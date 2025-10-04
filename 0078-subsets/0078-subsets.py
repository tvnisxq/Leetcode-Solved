class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        subset = []
        def dfs(i):
            # Base Case
            if i >= len(nums):
                result.append(subset.copy())
                return 

            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # Decision NOT to include nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return result