from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Initializes a defaultdict named anagramMap. If a key is accessed that doesn't exist it will automatically 
        # create a new entry with an empty list ([]) as it's value. 
        anagrmaMap = defaultdict(list)   

        # Looping through each string s in the input list of strings strs
        for s in strs:
            # And Creating a map of 26 entries and initializes all its elements as 0.
            # Each entry in this list will store the frequency of the corresponding lowercase english alphabet. 
            count = [0] * 26

            # Looping throug the individual string s to map the frequencies of the characters in that string
            for c in s:
                # According to the ASCII norms ord('a')(a being the very first character of the eng alphabets) is equal to 97 simiarly ord('z') = 122.
                # So if c = 'a' -> ord('c') - ord('a') = 0 & similarly the last character z maps to 25. Then it increments the count at that index in
                # in the count list.
                count[ord(c)-ord('a')] += 1
            # Print statement to print anagrmaMap dict.
            # print(anagrmaMap)

            # Type conversion of anagrmaMap dict from list to tuple 
            # Tuples are hashable and can be used as dictionary keys unlike lists in python.
            key = tuple(count)

            # Uses the key(the tuple of character frequencies) to add the current string s 
            # to the list associated with that key in anagramMap. If the key doesn't exist defaultdict automatically creates 
            # an empty list for it and then appends the string.
            anagrmaMap[key].append(s) 

        # Returns a list of all the values from the anagramMap dictionary.
        # Each value is a list of anagrams(string with same character frequencies), grouped together. 
        return list(anagrmaMap.values()) 

