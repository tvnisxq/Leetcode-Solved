# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # Approach 1(Brute Force):
        # Time: O(n.m) -> string lookup is linear
        # Space: O(1) -> only an integer variable 'count' is used

        # count = 0
        # for stone in stones:
        #     if stone in jewels:
        #         count += 1
        # return count


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        '''
        Approach 2(Optimal Method):
        - O(1) constant time lookup to check if something is in the set.

        Time: O(n+m) 
            - n to build the set  +
            - m to loop through the elements and doing O(1) lookups: O(m) total
        Space: O(n)
            - because of the n jewels which stores upto n characteres if all are unique.
            
        '''         
        setJewels = set(jewels)  #('a', 'A',...)

        count = 0
        for stone in stones:
            if stone in setJewels:
                count += 1
        return count
