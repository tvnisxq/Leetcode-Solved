class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openCount = 0
        additions = 0

        for ch in s:
            if ch == "(":
                openCount += 1
            else:
                if openCount > 0:
                    openCount -= 1
                else:
                    additions += 1
        return openCount + additions