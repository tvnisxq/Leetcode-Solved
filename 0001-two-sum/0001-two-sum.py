class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # '''
        #     Brute Force Approach:
        #         ▷ Time: O(n²) -> quadratic relationship between input size and run time.
        #                         If input size doubles, run time quadruples. n is the length 
        #                         of the nums array. 
        #         ▷ Space: O(n) -> uses a constant amount of auxiliary space, the space complexity is O(1).
        #                         It does not grow with input size.
        # '''
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)): # comparison & addition taking place -> O(1)
        #         if nums[i] + nums[j] == target:
        #             return [i,j]  



        '''
            Optimal Solution: Implementing Hashing
                ▷ Time: O(n) -> Only a single pass is required.
                ▷ Space: O(n) -> Map is used to store elements.     
        '''
        # Handling Edge Cases
        # ▷ Checks if nums is empty.
        # ▷ Checks if nums has fewer than 2 elements.    
        if not nums or len(nums) < 2: # If either of the above two cases are true - 
            return []                 # not possible to find two numbers that add up to target.

        # Creates an empty dictionary to store num:index as key:value pairs 
        numMap = {}
        # Enumerate provides position(i) & number(num) itself for each item in the list.
        for i, num in enumerate(nums):
            # Complement is the number that when added to num would result in target.
            complement = target-num 
            
            # Check if complement is already present in the map as key.
            # Meaning the number needed to reach the target has already been seen.
            if complement in numMap:
                # List is returned containing the index of complement & current index i.
                return [numMap[complement],i]
            # If the complement wasn't in numMap, it means the current number (num)
            # isn't part of a pair that has been found yet.
            # So it is added in the map for future reference.
            numMap[num] = i
        # If the loop finishes and no pair that adds up to the target has been found,
        # No such pair exists in the list -> We simply return an empty list.
        return []