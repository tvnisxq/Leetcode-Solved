# class Solution:
    # Brute Force Solution:
    # def findClosestNumber(self, nums: List[int]) -> int:
        # Initializing closest_distance as infinity so the first iteration
        # in the if statement is always True.
        # closest_distance = float('inf')
        # Result is initilized as the very first element of the array.
        # result = nums[0]

        # for num in nums:
            # calculates absolute distance of nums from 0.
            # distance = abs(num)

            # if distance < closest_distance: # True for first iteration.
            #     closest_distance = distance
            #     result = num

            # If distance equals closest_distance calculated yet 
            # and this num is greater than result. 
            # elif distance == closest_distance and num > result:
            #     result = num # then the result is updated to this num.

        # return result


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Approach 2: Not Optimal but:
        # • Shows fluency in python.
        # • Less verbose.
        # • Fewer lines of code and only 1 variable.
        # • Single condition handles both cases
        # • More readable once you can understand the logic.

        result = nums[0]

        for num in nums[1:]:
            # Key condition: Closer to 0 OR Same distance but larger value.
            if abs(num) < abs(result) or (abs(num) == abs(result) and abs(num) > result):
                result = num

        return result


# Approach 3: One Liner python code.
# class Solution:
#     def findClosestNumber(self, nums: List[int]) -> int:
#             return min(nums, key = lambda x: (abs(x),-x))


# Time: O(n) --> O(1) for initialisation, O(n-1) for iterations X O(1) per iteration.
# Space: O(1) --> No additional data structures used beside result and num variables.