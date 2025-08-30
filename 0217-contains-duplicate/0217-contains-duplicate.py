from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
            Optimal Approach:
                ▷ Time: O(n) -> n is the number of elements in the input list.
                ▷ Space: O(k) -> k is the number of unique elements.
        '''
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        for num, count in freq.items():
            if count > 1:
                return True
        return False