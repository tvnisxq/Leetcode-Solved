# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         '''
#             Moving Two Indices:
#             • Verbose method: we can make this more concise.
#             • if they don't match: only move index at i(index for t).
#             • if they do: move both indices(index for t and index for s).

#         '''        
#         S = len(s)
#         T = len(t)

#         # Edge case: if s is empty, it's always a subsequence
#         if s == '': return True 

#         # Edge case: if len(s) > len(t) -> there's no way it can be a   
#         # subsequence.
#         if S > T: return False # A subsequence can never be longer than it's parent string. 
                                
#         # However, if above cases are not satisfied: This means that T is atleast equal in length to S.

#         j = 0 # initilaze a pointer for s

#         for i in range(T):
#             if t[i] == s[j]:  # since matching move both.
#                 if j == S-1:  # if j has reached the end of the string.
#                     return True

#                 # if above case is not true but they still match.
#                 j += 1  # we don't need any explicit increment for i(it will always move via loop).

#         # If our loop makes it to the end and any of the above conditions are not satisfied: Its not a subsequence
#         return False
                        
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
            Concise Approach:
            • removes redundant checks
            • combines the logic for checking if all characters in s are found.    
        '''

        # Check if s is an empty string:
        if not s: return True

        # Check is s is longer than t:
        # A subsequence cannot be longer than it's parent string.
        if len(s) > len(t): return False

        # Initialize pointer for tracking characters in s:
        j = 0

        # Looping through characters in t:
        for char in t:
            if j < len(s) and char == s[j]:
                j += 1 # match found move the pointer one step ahead.

        # returns True if len(s) equal value of j after complete iterations.
        # since the return type is bool -> converts a valid condition to True.

        return len(s) == j # True if all characters in s we're found in order.  

