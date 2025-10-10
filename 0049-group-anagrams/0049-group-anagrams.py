from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramMap = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagramMap[key].append(s)
        
        return list(anagramMap.values())