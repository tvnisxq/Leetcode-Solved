class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0 

        for i in range(n):
            ax, ay = points[i]
            for j in range(n):
                if i == j:
                    continue

                bx, by = points[j]

                if not (by >= ay and bx <= ax):
                    continue
                
                found = False
                for k in range(n):
                    if i == k or j == k:
                        continue
                    cx, cy = points[k]
                    if bx <= cx <= ax and by >= cy >= ay:
                        found = True
                if not found:
                    count += 1

        return count