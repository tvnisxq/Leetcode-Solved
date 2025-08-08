from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Using defaultdict to avoid missing character key frequencies.
        freq_count = defaultdict(int)

        # Iterating through the nums array to add num frequencies
        for num in nums:
            freq_count[num] += 1
            # print(freq_count) # To check whether freq_count is created successfully.

        # Iteratimg through the freq_count to check for count.
        for num, freq in freq_count.items():
            if freq_count[num] > n/2:
                return num
            

                    