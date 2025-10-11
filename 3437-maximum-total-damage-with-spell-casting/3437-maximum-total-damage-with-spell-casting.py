from collections import defaultdict
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        fm = defaultdict(int)
        for x in power: fm[x] += 1
        unique = sorted(list(fm.keys()))

        n = len(unique)
        dp = [0] * n
        mx, j = 0, 0

        for i in range(n):
            while j < i and unique[j] < unique[i]-2:
                mx = max(mx, dp[j])
                j += 1
            dp[i] = mx + unique[i] * fm[unique[i]]

        return max(dp)


