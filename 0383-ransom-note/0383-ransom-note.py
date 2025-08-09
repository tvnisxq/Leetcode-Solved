# Approach 1: Best for Interviews
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for c in magazine:
            if c in counter:
                counter[c] += 1  # 1 higher frequency of the already existing character.
            else:
                counter[c] = 1    # Set the frequency of that very character to 1 
                                  # if it doesn't exist
        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else:
                counter[c] -= 1
        return True






# Approach 2: Using defaultdict
'''
This takes a parameter(takes the parameter as what you want to make the value as a defualt) 
defaultdict creates an entry of the character c in the defaultdict:
    if the character is not in the dict:    
        creates a entry of c as 0 and immediately
        increments it to 1(cuz now we have seen it).
    else: (character exists in the dict)
        immediately increments it by 1 as now we have
        seen the same character that already exists.
'''
from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(int)
        for c in magazine:
            counter[c] += 1

        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c] 
            else:
                counter[c] -= 1 
        return True






# Approach 3: using python's built-in counter module
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine) # Creates a dict from magazine characters 
                                    # where keys are characters and values are the occurence 
                                    # frequencies of the characters.
        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else:
                counter[c] -= 1
        return True
