class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            # Check if n is the start of a sequence
            if (n-1) not in numSet:
                length = 0
                # Initially length = 0 so we're checking the 1st number
                while (n + length) in numSet: 
                    # As the length grows we consecutively check more numbers
                    length += 1
                longest = max(longest, length)
        
        return longest