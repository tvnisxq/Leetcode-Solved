# Solution 1: Cleaner and Concise
# • makes use of (n + length) in the while loop directly
# • Enhanced readability
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            # check if n is the start of a sequence:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet: # Initially length = 0, so were checking the first number.
                    length += 1   # As the length grows, we consecutively check more numbers.   
                longest = max(length, longest)
        return longest



# Solution 2: A little verbose
# • Adds +1 manually
# • Readability is good but wordier
# • Extra next_num variable adds slight complexity 
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums)
#         longest = 0
#         for num in nums:
#             if (num-1) not in numSet:
#                 next_num = num + 1
#                 length = 1
#                 while next_num in numSet:
#                     length += 1
#                     next_num += 1
#                 longest = max(longest, length)
#         return longest


# Time: O(n)  -> because you go through the numbers and you only 
#                execute nested while if n starts a sequence
# Space: O(n) -> Space complexity comes from the set. We're basically storing 
#                n elements