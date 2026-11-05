class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Look-ahead Forward Scan
        """
        dict_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        i, sum = 0, 0
        n = len(s)
        total = 0

        while i < n:
            # Check if current character is less than next
            if i < n-1 and dict_roman[s[i]] < dict_roman[s[i+1]]:
                sum += dict_roman[s[i+1]] - dict_roman[s[i]]
                i += 2 # skip the current and the next character(both are processed)
            else:
                sum += dict_roman[s[i]]
                i += 1

        return sum
       