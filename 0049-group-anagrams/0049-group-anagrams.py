from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        we use defaultdict to avoid having to initialize an empty array
        for your keys every single time. Provides an empty array or any 
        other data structure assigned to a key by default.
        """
        
        # Initialize an empty hashMap using List
        anagramMap = defaultdict(list)
        # Result will be stored in an empty array
        result = []

        for s in strs:
            # Sorted method returns back a list which is mutable data type 
            # and mutable data types can't be keys
            sorted_s = tuple(sorted(s)) # Sorts string in alphabetically increasing order and converting type to tuple 
            anagramMap[sorted_s].append(s) # adding a sorted version of that as a key in the map
            # print(anagramMap)

        """ 
        For adding all the values in the map
        and appending them in the result.
        Iterating over all the values in the map -> returns the list of values
        """ 
        for value in anagramMap.values():
            result.append(value)
        return result