class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        for num, count in freq.items():
            if count > 1:
                return True  
        return False

        '''
            Time:
                • Best case: O(1)
                • Worst case: O(n)
        '''


        # Using hashsets
        # Create an empty hashset to store seen elements.
        freqSet = set()

        # Iterate through the nums array.
        for num in nums:
            if num in freqSet:
                return True     # Duplicate found
            freqSet.add(num)    
        return False            # No Duplicates Exist

        # Is there any more ways to achieve this?
        # NO this is the most optimal Approach to solve this with:
        '''
            Time: O(n) -> Only a single pass is required.
            Space: O(n) -> In the worst case(all elements are unique) we need to store n elements. 
        '''
