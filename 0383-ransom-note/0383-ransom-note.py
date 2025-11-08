from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictMag = defaultdict(int)

        for m in magazine:
                dictMag[m] += 1
        
        for r in ransomNote:
            if dictMag[r] <= 0:
                return False
            dictMag[r] -= 1
        
        return True