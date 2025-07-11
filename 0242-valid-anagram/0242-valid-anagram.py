class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If two strings are different they cannot be anagrams.
        if len(s) != len(t):
            return False 
        '''
            Initializes an empty dictionary. This wil be used
            to store the frequency(number of occurences) of 
            different characters in the string.
            '''      
        map = {}

        for c in s:
            '''
            Gets the current count of c from the dictionary.
            If c is not in the dictionary yet, it returns 
            0(default value).
            Then it adds 1 to the count, and stores in the dictionary.
            ''' 
            map[c] = map.get(c, 0) + 1

        for c in t:
            if c not in  map or map[c] == 0:
                return False
            map[c] -= 1

        return True

            