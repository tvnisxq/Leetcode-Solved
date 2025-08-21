class Solution:
    def isPalindrome(self, x: int) -> bool:
        # palindromes can't be negative
        if x < 0: return False

        # Number with which x is to be divided so chopping of left & right digits can be done
        div = 1
        while x >= div * 10:
            div *= 10

        # Main loop that continues until x is not 0.        
        while x:
            right = x % 10 # Extracts the rigthmost digit of x using the modulo operator.
            # div is a power of 10 that aligns with x.
            left = x//div # Extracts the leftmost digit of x using the integer division


            # Checks if the leftmost & rightmost digit are not equal.
            if left != right: return False # returns False if they're unequal.
            '''
            Updates x by removing both the leftmost & the rigthmost digit.
                • x % div -> removes the leftmost digit by taking the remainder(after dividing by div).
                • // 10 -> removes the rightmost digit by performing integer division by 10.
            '''
            x = (x % div) // 10 
            
            # This updates div by dividing it by 100. Since two digits(leftmost & rightmost are removed from x in each iteration)
            #, div needs to be adjsuted to accurately target the new leftmost digit.
            div = div//100
        return True
        