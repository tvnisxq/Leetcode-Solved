class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(potions)
        potions.sort()

        def binarySearch(s):
            l = 0 
            r = m - 1
            while l <= r:
                mid = l + (r-l) // 2
                if potions[mid] * s >= success: r = mid - 1
                else: l = mid + 1
            return l

        res = []
        for s in spells:
            res.append(m - binarySearch(s))
        return res