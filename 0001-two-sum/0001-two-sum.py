class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            Brute Force Approach:
                ▷ Time: O(n²) -> quadratic relationship between input size and run time.
                                If input size doubles, run time quadruples. n is the length 
                                of the nums array. 
                ▷ Space: O(n) -> uses a constant amount of auxiliary space, the space complexity is O(1).
                                It does not grow with input size n.
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): # comparison & addition taking place -> O(1)
                if nums[i] + nums[j] == target:
                    return [i,j]  
