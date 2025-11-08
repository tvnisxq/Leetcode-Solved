class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictMag = defaultdict(int)
        
        # Loop over the characters of magazine
        for m in magazine:
            dictMag[m] += 1 # increment the count of characters as we see them 
        
        # Loop over the chars of ransomNote
        for r in ransomNote:
            if dictMag[r] <= 0: # if char count is negative or zero we can't use it
                return False
            dictMag[r] -= 1 # otherwise just decrement the char count for next iteration
        
        # if all chars of ransomNote are completed using 
        # chars of magazine, 
        return True