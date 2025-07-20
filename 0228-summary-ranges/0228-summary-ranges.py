# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
        
#         # Empty List to store the result.
#         result = []
#         # Variable to keep track of the traversed List elements:
#         i = 0

#         # Looping through elements as long as i value is less than len(nums).
#         while i < len(nums):
#             start = nums[i]  # Assigning the very first element as the start.

#             # Inner loop:
#             '''
#                 • 1st Condition: Ensures we're not checking any element beyond the bounds of nums.
#                 • 2nd Condition: Checks if the next number we're looking at is contigous to the current.    
#             '''
#             while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
#                 i += 1  # Increment i by 1 if both values hold true.

#             # If the number assigned to start is not equal to nums[i](i representing the last iterable index).
#             # Then the numbers start & i are forming a range. 
#             if start != nums[i]:
#                 result.append(str(start) + '->' + str(nums[i])) # Appeding the range to result List.
                
#             # However if they both are equal.
#             # Then this number is not a range but a single number.
#             else:
#                 result.append(str(nums[i])) # Push this single number in the result List.

#             i += 1 # Increment the value of i by 1 no matter what
        
#         return result


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        # Check if nums is an empty list.
        if not nums: 
            return []
        # Initialize result & i as empty list and 0 respectively.
        result , i = [] , 0

        # Outer loop: iterates as long as i value is less than len(nums):
        while i < len(nums):
            # Assign i value to start.
            start = i # start = i = 0

            # Inner loop:
            ''' 
               • 1st condition: ensures we're not checking an element which is not present.
               • 2nd condition: checks if the next number we're looking at is contiguous to the current.
            '''
            while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                i += 1 # increment i if and only if both conditions are satisfied.
            
            # If start equals i: append it as a single number.
            # If not: append it as a range of start -> i.
            result.append(f"{nums[start]}" if start == i else f"{nums[start]}->{nums[i]}")
            i += 1  # increment i value to check for next element

        return result
