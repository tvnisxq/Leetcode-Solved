class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if len(s) > len(t): return False

        j = 0
        for char in t:
            if j < len(s) and char == s[j]:
                j += 1
        
        return len(s) == j