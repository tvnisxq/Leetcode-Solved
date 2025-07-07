# Brute Force Solution:
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         result = []

#         for i in range(n):
#             product = 1

#             # First inner loop: multiply all indices before index i
#             for j in range(i):
#                 product *= nums[j]

#             # Second inner loop: multiply all indices after index i
#             for j in range(i+1, n):
#                 product *= nums[j]

#             result.append(product)
        
#         return result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # First Pass: Calculate Prefix products.
        # Product of all the elements to the left of a given element.
        # Assume left index = 1.  
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Second Pass: Calculate Suffix products and multiply.
        # Product of all the elements to the right of the array.
        # At last element assume last element = 1.
        # Multiply prefix and suffix products.   
        suffix = 1
        for i in reversed(range(n)):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer        