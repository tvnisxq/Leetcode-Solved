# Brute Force
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i] == nums[j]:
#                     return True
#         return False



# Optimal Approach
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty hashset to store seen elements
        seen = set()

        # Iterate through the elements:
        for num in nums:
            if num in seen:
                return True    # Duplicate Found
            seen.add(num)
        return False           # No Duplicates Exist 