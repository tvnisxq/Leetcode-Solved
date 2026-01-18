from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            outgoing[src] += 1
            incoming[dst] += 1

        # Incoming must be n-1 and outgoing must be 0
        for i in range(1, n+1):
            # Meaning the town judge trusts nobody(including himself: 0)
            # and everybody in the town trusts him except himself(n-1).
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i
        return -1

# Time: O(v+e)
# Space: O(v)