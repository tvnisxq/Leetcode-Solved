class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            Optimal Approach:
                • Time: O(n+n+1) = O(2n + 1) = O(n)
                • Space: Memory used by the algorithm is primarily for the map dictionary. 
        '''

        # Initial Check: If strings are of diferent lengths they can't ever be anagrams.
        if len(s) != len(t):   # constant time operation to check string lengths: O(1)
            return False
        
        # Creating a defaultdict to keep track of character frequnencies
        map = {}    # constant time operation to create a dictionary: O(1)

        # looping and storing chars of s: O(n)
        for c in s:
            map[c] = map.get(c,0) + 1 # dictionary lookup and addition both of which are constant time opeartions on average: O(1) 

        # looping through chars in t to check if they're anagrams
        # This loop runs n times where n is the length of t: O(n)
        for c in t:
            if c not in map:  # checking for key existence is a constant time operation: O(1) 
                return False
            map[c] -= 1     # updates value in the dictionary: O(1)
        
        # To check if all the characters of s are used by t to create an anagram
        # In the worst case a dictionary can contain 26 lowercase eng alphabets(constant & independent of input string length): O(1)
        for val in map.values():
            if val != 0:
                return False
        return True



        