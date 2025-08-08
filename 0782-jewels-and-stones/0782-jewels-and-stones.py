from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        '''
            Brute Force Approach:
                If n = len(stones) & m = len(jewels)
                ▷ Time: O(n.m) -> Iterating through stones and jewels once. String lookup is linear 
                ▷ Space: O(1) -> Only a variable count is used.
        '''
        count = 0
        # Iterating through string literal stones character by character
        for stone in stones:
            # if that very character is also present in the string literal jewels. 
            if stone in jewels:
                count += 1 # Increment the count varaible by 1.
        return count