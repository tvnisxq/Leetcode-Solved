class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
            Two methods:
            ▷ 1. Two pointers: Cheat method.
            ▷ 2. Two pointers: Cheat method short.
            ▷ 3. Two pointers: function creation to handle alphanumeric characters.
        '''
        # ▷ CHEAT METHOD
        # Initializing two pointers:
        n = len(s)
        l = 0
        r = n - 1 

        # Loop runs until left and right pointers converge at a common point.
        while l < r:
            # This is where we cheat by using the builtin .aplhanum python function.
            # If the character at l is not an alphanumeric:
            if not s[l].isalnum():
                l += 1 # move the left pointer one step ahead
                continue 
            # If the character at r is not an aplhanumeric:
            if not s[r].isalnum():
                r -= 1 # move the right pointer one step ahead(from the end)
                continue
            
            # If the lowercase of character at l is not same as lowercase 
            # of the character at r -> they're not a palindrome 
            if s[l].lower() != s[r].lower():
                return False # hence return False

            '''
            Moving the pointers inward either way cuz the loop will terminate 
            only when they converge at a common point. This is for moving past a valid,
            matching pair of characters
            '''
            l += 1
            r -= 1

        return True