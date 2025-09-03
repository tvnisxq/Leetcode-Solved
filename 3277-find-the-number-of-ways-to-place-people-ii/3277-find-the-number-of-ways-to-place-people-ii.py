class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: x[1], reverse=True)
        points.sort(key=lambda x: x[0])

        result = 0

        for i in range(n):
            mxy = points[i][1]
            mny = float('-inf')
            for j in range(i+1, n):
                _, y = points[j]
                if mny < y <= mxy:
                    mny = y
                    result += 1
        return result
