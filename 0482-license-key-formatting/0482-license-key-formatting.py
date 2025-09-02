class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        s = s.replace("-", "")
        s = s[::-1]

        result = []
        for i in range(0, len(s), k):
            result.append(s[i:i+k])
        return "-".join(result)[::-1]