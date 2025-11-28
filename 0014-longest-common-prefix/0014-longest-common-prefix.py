class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # this determines the no. of iterations
        min_length = float('inf')

        # Looping through strings in strs.
        for s in strs:
            # if length of string is less than our min_length:
            if len(s) < min_length:
                min_length = len(s) # update the min_length

        i = 0 
        # this loop runs until i becomes equal to the min_length
        while i < min_length:
            for s in strs:
                # check if the character at ith index of string s is
                # also present in the same index in the first string of strs.
                if s[i] != strs[0][i]:
                    # mismatch found: condition=True
                    # ---> returns the common char up until the last iterated i.
                    return s[:i]
            i += 1
        # return empty string if no match is found
        return strs[0][:i]