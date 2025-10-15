class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # First calculate all the prefix products
        # Product of all the elements to the left of a given element
        # Assume left index = 1.
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Second Pass: Calculate suffix products and multiply
        # Product of all the elements to the right of the array
        # At last element assume last element = 1
        # Multiply prefix and suffix products
        suffix = 1
        for i in reversed(range(n)):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
