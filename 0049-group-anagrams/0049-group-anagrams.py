from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        we use defaultdict to avoid having to initialize an empty array
        for the keys every single time. Provides an empty array or any 
        other data structure assigned to a key by default
        """
        # Initialize and empty hashmap using list
        anagramMap = defaultdict(list)

        # Result will be stored in an empty array
        res = []

        for s in strs:
            # Sorted method returns back a list which is mutable data type 
            # and mutable data types can't be keys
            # sorts strings in alphabetically increasing order and 
            # converting them to a tuple
            sorted_s = tuple(sorted(s))

            # Adding a sorted version of that as a key in the map
            anagramMap[sorted_s].append(s)

        # For adding all the values in the map and appending them in the result. 
        # Iterating over the values in the map
        for value in anagramMap.values():
            res.append(value)
        return res

