class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """Brute Force Approach"""
        # count = 0
        # for stone in stones:
        #     if stone in jewels:
        #         count += 1
        # return count

        """ Optimal Approach"""
        # setJewels = set(jewels)
        # count = 0
        # for stone in stones:
        #     if stone in setJewels:
        #         count += 1
        # return count

        """One Liner Pythonic Approach"""
        return sum(stone in set(jewels) for stone in stones)