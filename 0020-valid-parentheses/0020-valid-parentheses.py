class Solution:
    def isValid(self, s: str) -> bool:
        '''
            Brute Force:
                ▷ Time: 
                    • each iteration scans entire string - O(n)
                    • maximum n/2 iterations needed - O(n)
                        TOTAL: O(n²)
                ▷ Space:
                    replace() method creates a new string every time it's called bcoz strings in python cannot be changed in place.
                    The largest string you ever hold in memory during this algorithm is the original one (size n).
                    Since .replace() allocates a new string while the old one is still in memory, peak memory usage is: O(n) + O(n)
                        TOTAL: O(2n) -> O(n)
        '''
        # keep removing valid characters until there are none left
        while True: 
            true_length = len(s) # len function of string has a constant time complexity: O(1)

            s = s.replace('()','')    
            s = s.replace('{}','')    
            s = s.replace('[]','')

            # If no change is made it's a valid parenthesis.
            if len(s) == true_length:            
                break

        return len(s) == 0 