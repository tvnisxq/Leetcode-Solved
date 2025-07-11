class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        Brute Force Method: Using String Comcatenation.
            • Time: O(n + m); n = len(word1) & m = len(word2)
            • Core Concept used can also be said as two pointers
        '''

        result = '' # Initialize an empty string for storing result
        Set up 2 pointers to track positions in word1 & word2.
        i = 0 
        j = 0

        # The main loop runs until both pointer's Indices run out of bound.
        while i < len(word1) and j < len(word2):
            Adding to the result
            result += word1[i]
            result += word2[j]
            # Incrementing the pointers by 1.
            i += 1 
            j += 1

        # Add remaining characters from word1.
        while i < len(word1):
            result += word1[i]
            i += 1

        # Add remaining charactes from word2.
        while j < len(word2):
            result += word2[j]
            j += 1

        return result

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        Otimal Approach 1(Better): List append/ Two Pointers. 
        • List append is O(1) amortized, while string concatenation can be O(n) in worst case.
        • Same alternating logic but using List.append() which is O(1).
        • Converting List to string at the end to store result.
        • Same Time and Space Complexity as above.
        • USE THIS FIRST DURING LIVE INTERVIEWS: Then optimize, if asked and time permits.
        '''
        result = []
        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        
        # Add remaining characters from word1:
        while i < len(word1):
            result.append(word1[i])
            i += 1

        # Add remaining characters from word2:
        while j < len(word2):
            result.append(word2[j])
            j += 1
        
        # Conversion of List result to String result.
        return ''.join(result)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        Optimal Approach 2(Using Single loop):
        • Concise and less wordier.
        • Clever solution.
        • Use this after the optimal two pointers approach t optimize further(IF ASKED).
        '''
        result = []
        # calculate max length of both the strings.
        # This determines how many iterations our loop needs.
        max_len = max(len(word1), len(word2))

        # Single loop that runs for max_len iterations
        # This replaces the need for multiple while loops.
        for i in range(max_len):
            # Check if current index i is within bounds of word1.
            # Prevents IndexError when word1 is shorter than word2.
            if i < len(word1):
                result.append(word1[i]) # Add characters from word1 at index i.
            
            # Check if current index i is within bounds of word2.
            # Prevents IndexError when word2 is shorter than word1.
            if i < len(word2):
                result.append(word2[i]) # Add characters from word2 at index i.
                
        return ''.join(result)

