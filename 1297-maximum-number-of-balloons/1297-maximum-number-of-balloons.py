from collections import defaultdict
class Solution:
    '''
        Approach 1: Slightly verbose and Basic.
            We use defaultdict to to solve this question because accessing a missing key 
            in defaultdict won't raise an IndexError -> As the missing keys are automatically created and assigned a 
            default value(0 in case of integers).
    '''
    def maxNumberOfBalloons(self, text: str) -> int:

        counter = defaultdict(int)
        balloon = "balloon"

        # For every character in text, check if that character also is in the balloon.
        for c in text:
            if c in balloon:
                counter[c] += 1
                '''
                    If that character is not in the balloon, defaultdict automatically creates a 
                    key of that character in the dictionary and immediately increments it by 1.

                    However, if the character was already present in the dictionary it just performs normal increment on them. 
                '''
        # Check whether any character in balloon is missing from the counter.
        if any(c not in counter for c in balloon):
            return 0  
            '''
                No instances of balloon can be created since a character which was required to make a balloon(or more than one      
                balloons) is/are not present. 
            '''
        else:
            return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])


from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> bool:
        '''
            Approach 2: Clean & Concise(BETTER FOR INTERVIEWS)
                • Short, Clean & expressive
                • Designed exactly for this use case
                • Makes you look fluent in python
        '''
        count = Counter(text)
        return min(
            count['b'],
            count['a'],
            count['l']//2,
            count['o']//2,
            count['n'],
        )

            
