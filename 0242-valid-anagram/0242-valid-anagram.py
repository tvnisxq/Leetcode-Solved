class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        map = {}
        for c in s:
            map[c] = map.get(c,0) + 1

        for c in t:
            if c not in map:
                return False
            map[c] -= 1
        
        for val in map.values():
            if val != 0:
                return False
        return True


