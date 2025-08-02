# Approach 1: Slightly Verbose

# This approach is slightly verbose and basic.
# We use default dict to solve this question because: Accessing a missing key
# doesn't raise an error — assigns default value of 0.
# from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = 'balloon'

        # for every character in text 
        # check if that character also is in the balloon.
        for c in text:
            if c in balloon:
                counter[c] += 1  
                '''
                • if that character is not in the balloon, deafaltdict creates
                a key of that character and immediately increments its value to 1 which was 
                0 by default.

                • if it is present in the balloon, increments it by 1. 
                '''
        # Checks whether any character
        # in balloon is missing from counter.
        if any(c not in counter for c in balloon):
            return 0        # no instances of balloon can be created
                            # since a character which is required to create balloon(or more than one ballons)
                            # is missing from the dictionary/not sufficient. 
        else:
            return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])

# Approach 2: Clean and Concise(better for interviews)

# • Short, clean, expressive
# • Designed exactly for this use case
# • Makes you look fluent in Python

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n'],
        )
            
