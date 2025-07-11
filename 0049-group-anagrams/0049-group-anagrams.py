from typing import List
from collections import defaultdict
class Solution:
    """ 
    we use defaultdict: TO avoid having to initialize an empty array for your keys
    every single time. Provides an empty array or other data structure assigned to a key 
    by default. 
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary where each key maps to a list of anagrams.
        anagramMap = defaultdict(list)

        # Loop over each string in the input list.
        for s in strs:
            # Create a count array for current string
            # Initialize the count array for 26 lowercase letters all with 0s
            count = [0] * 26 

            '''
            For each character c in String s:
            # Convert c to its alphabetical index ord('a') = 97.
            # ord(c) - ord('a') maps 'a' to 0 and 'z' to 25.
            # Nested loop: over each character of the current string(builds frequency count for current string)
            '''
            for c in s:
                count[ord(c) - ord('a')] +=1
            # Print statement to check the created hashMap of tuple
            # print(anagramMap)

            #Convert character count to a hashable key
            key = tuple(count)

            #Group anagrams uisng the key
            anagramMap[key].append(s)
        
        #Return grouped anagrams as list of lists
        return list(anagramMap.values())
