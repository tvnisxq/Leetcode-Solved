class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # '''
        # Brute Force Approach:
        # '''
        # # Check if the lengths of both strings are equal
        # if len(s) != len(t): # two strings can be anagrams only if they are of equal lengths.
        #     return False     # return False if they are not.
        
        # '''
        #     TIME:
        #     The return type is given as bool.
        #     So if the conditon that sorted strings are equal is satisfied, True is returned and False otherwise.
        #     Python's sorted function uses Timsort -> a derivation of merge and insertion sort combined which has a worst 
        #     case time complexity of O(N log N), where N=len(string). So total = O(N log N + M log M).
        #     But since the strings are of equal lengths(initial check) -> O(N log N).

        #     After sorting comparison of two sorted lists is taking place O(N). However this is 
        #     dominated by sorting step SO OVERALL TIME COMPLEXITY DOESN'T CHANGE.

        #     SPACE:
        #     Sorted function in python returns a new list with sorted elements. Requires additional space to store 
        #     these new lists. Timsort has a worst case space complexity of O(N). But here two strings are being sorted 
        #     so it becomes O(N + M). Since the strings here are of same length -> O(N)
        # '''   
        # return sorted(s) == sorted(t) 

        '''
            Optimal Approach:(Using a Map)
            • Time: Only a single pass is required. O(n).
            • Space: Assuming ASCII character set O(1).
        '''

        # Check the lengths of the strings:
        if len(s) != len(t): # anagrams must be of equal lengths
            return False

        # map to store the frequency counts of the character    
        map = {}

        for c in s:
            # Fetches the current char value and:
            '''
                • If the char already exists -> increments the value by 1.
                • If char is not already present -> assings it default value 0 and '+1'
                immediately adds 1 to the 0 making it 1(since now the element now has been seen).
            '''
            map[c] = map.get(c,0) + 1

        for c in t:
            if c not in map:
                # all characters of 't' must be present in the map
                # in order to check if 't' is an anagram of 's'. 
                return False
            # If c in the map -> reduce it's count
            # ANALOGY: This character has been used to create 't' from 's'.
            map[c] -= 1

        for val in map.values():
            # If all char counts become 0, it means all characters of 's'
            # has been used to create anagram 't'. Therefore, Valid Anagram.
            if val != 0:
                return False
        # If the loop finishes, it means all values in map.values are indeed 0 -> return True.
        return True