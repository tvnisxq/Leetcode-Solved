class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        abs_x = abs(x-z)
        abs_y = abs(y-z)

        if abs_x < abs_y: return 1
        elif abs_x > abs_y: return 2
        else: return 0
            