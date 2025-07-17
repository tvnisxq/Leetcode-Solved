class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # This determines the number of iterations.
        min_length = float('inf')
        
        # looping through strings in strs.
        for s in strs:
            # if length of a string is less than than our min_price;
            if len(s) < min_length:
                min_length = len(s)  # update our min_price
        
        i = 0
        # This loop runs until i becomes equal to the min_length.
        while i < min_length:
            for s in strs:
                # check if the character at ith index of string s is also present in the same index in the first string of strs.
                if s[i] != strs[0][i]:
                    # mismatch found: condition = True.
                    # returns the common character up until the last iterated i.
                    return s[:i]
            i += 1
        # s[:i] returns empty string if no match is found.
        return s[:i] 



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Initial Check: To check if the string array is empty:
        if not strs: 
            return ""   
        
        # The range for this loop is whatever the length of the first string in strs is..
        for i in range(len(strs[0])):
            char = strs[0][i]

            # check if other strings are of length equal to or greater than
            # index i. 
            '''OR''' 
            # character at ith index of string is not eqaul to the variable 'char'.
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]
        
        # if no match is found this return statement gets executed.
        # it means the enture first string is a prefix in all other strings.
        # so return the whole first string.
        return strs[0]
