class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        longest_pal = 0

        for i in range(len(s)):
            # Odd length palindromes
            l , r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l +  1) > longest_pal:
                    res = s[l:r+1]
                    longest_pal = r - l + 1
                l -= 1
                r += 1
            
            # Even length palindromes
            l, r = i, i+1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest_pal:
                    res = s[l:r+1]
                    longest_pal = r - l + 1
                l -= 1
                r += 1
        return res