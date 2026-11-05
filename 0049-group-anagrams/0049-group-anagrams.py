from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Empty answer to store the result
        answer = []
        # Initialize an empty hashmap of lists
        anagram_map = defaultdict(list)

        # Iterating over each string
        for s in strs:
            # Storing the strings and converting them to an immutable data type: tuple
            sorted_s = tuple(sorted(s)) # {'a', 'e', 't'}

            # Adding a sorted version of that as a key in the map
            anagram_map[sorted_s].append(s) # {'a', 'e', 't': ['eat']}
        
        for values in anagram_map.values():
            answer.append(values) # ['eat', 'tea', 'ate', 'tan', 'nat', 'bat']
        return answer