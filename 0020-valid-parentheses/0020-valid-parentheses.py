# class Solution:
#     def isValid(self, s: str) -> bool:
#         '''
#             Brute Force:
#                 ▷ Time: 
#                     • each iteration scans entire string - O(n)
#                     • maximum n/2 iterations needed - O(n)
#                         TOTAL: O(n²)
#                 ▷ Space:
#                     replace() method creates a new string every time it's called bcoz strings in python cannot be changed in place.
#                     The largest string you ever hold in memory during this algorithm is the original one (size n).
#                     Since .replace() allocates a new string while the old one is still in memory, peak memory usage is: O(n) + O(n)
#                         TOTAL: O(2n) -> O(n)
#         '''
#         # keep removing valid characters until there are none left
#         while True: 
#             true_length = len(s) # len function of string has a constant time complexity: O(1)

#             s = s.replace('()','')    
#             s = s.replace('{}','')    
#             s = s.replace('[]','')

#             # If no change is made it's a valid parenthesis.
#             if len(s) == true_length:            
#                 break

#         return len(s) == 0 


class Solution:
    def isValid(self, s: str) -> bool:
        '''
            Optimal Solution: Implementing Stack(LIFO Order)
            • For multi-type parenthesis check we need to implement stack to solve this.
            • For each closing bracket character in string s, we check if there's a 
            corresponding opening bracket character exists in our map.
            • This is the most optimal solution.

            ▷ Time: Single pass through string, each character is passed exactly once.
                    stack operations push/pop are constant time O(1).
            
            ▷ Space: Stack can hold upto n/2 characters in worst case

        '''

        # Initialize an empty list which acts as our stack
        stack = []

        # key:value  -> closing:opening
        mapping  = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        # Iterating through the string s 
        for char in s:
            # Check if this character is a closing bracket
            if char in mapping:
                # not stack: If stack is empty: there's no opening bracket to match -> return False
                # OR if stack.pop: remove & return the most recent opening bracket and match it with
                # the value of our current char mapping() -> if they are not same: return False
                # MEANING: if the popped character is not equal to the fetched opening bracket: return False 
                if not stack or stack.pop() != mapping[char]:
                    return False

            # If its not a closing bracket, it must be an opening bracket 
            else:
                # Append that character in the stack for next operations/flow of code.
                stack.append(char)

        # Since return type is bool: If len(s) == 0,
        # If it's true that length of stack is 0 -> return True otherwise false.
        return len(stack) == 0

