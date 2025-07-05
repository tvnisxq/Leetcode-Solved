# Brute Force: using Nested Loops
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         for i in nums:
#             if nums.count(i) > len(nums)/2:
#                 return i

'''
    Time: O(n²): counting frequency using nested loops.
    Space: O(1): just a few temporary variables are used.
'''
# Optimal solution: Using Boyer Moore Voting Algorithm
'''
When to use:
    • If an element occurs more than n/2 times, it will always be the last one standing after
    pairing off different elements.

    • Used When:
        • Majority element is required(Or in cased where it
        is given majority element is occuring > n/2 times) 

        • Dominant element is required.    

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Used to track the occurences of elements. 
        count = 0

        # Placeholder for the potential majority element.
        # will be updated throughout the loop based on the current count.
        candidate = None

        # Iterate therough entire list to check
        # what the majority element(candidate) is.
        for num in nums:
            # if count drops to 0: -> no candidate
            # therefore we assign a new one.
            if count == 0:
                candidate = num
            # if current number == candidate -> count += 1 else: count -= 1.    
            count += (1 if num == candidate else -1)
        # only element standing with count > 0 will be the majority element. 
        return candidate

# Eventually the real majority element will survive as it is guaranteed to be 
# occuring more than n/times, so it will always outweigh others.

'''
    Time: O(n): Only using one pass through the array.

    Space: O(1): we only use two vatiables(count & candidate)
                 regardless of the size of the input array.
'''