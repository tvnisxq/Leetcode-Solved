class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
            Two pointer approach:
        '''
        # taking the length of the string.
        n = len(s)
        '''
        Initializing the two pointers:
        one in the start index & the other in the last
        '''
        l = 0
        r = n - 1

        # Loop runs until the left pointer & right pointer becomes equal:
        while l < r:
            s[l], s[r] = s[r], s[l]
            # incrementing the left & right pointers
            l += 1
            r -= 1
