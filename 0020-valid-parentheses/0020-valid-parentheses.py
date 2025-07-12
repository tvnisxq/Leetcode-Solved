# class Solution:
#     def isValid(self, s:str) -> bool:

#         '''
#             Brute Force Solution:
#             • Time: O(n²) 
#                 - Each iteration scans entire string -> O(n).
#                 - Maximum n/2 iterations needed -> O(n)
#                 Total: O(n²)

#             • Space: O(n) for string operations.
#         '''
#         # keep removing valid characters until there are no changes.
#         while True:
#             original_length = len(s)

#             # Remove valid pairs.
#             s = s.replace('()', '')
#             s = s.replace('{}', '')
#             s = s.replace('[]', '')

#             # If no change is made: It's a valid parentheses.
#             if len(s) == original_length:
#                 break

#         return len(s) == 0




class Solution:
    def isValid(self, s: str) -> bool:
        '''
            Implememting Stack(LIFO order):
           • For multi type parentheses check we need to use stack to solve this.
           • For each closing bracket character in string s, we check if it's corresponing 
            opening character exists in our map.
           • This is the most optimal solution.


           Time: O(n)  
            - Single pass through string, each character is processed exactly once.
            - Stack operations push/pop are O(1).

           Space: O(n)
           - Stack can hold up to n/2 opening brackets in worst case.
        '''
        # Initialize empty List which acts our stack:
        stack = []
        mapping = {
            ')': '(', ']':'[', '}': '{'  # key:value -> closing: opening
        }

        for char in s:
            # check if this character is a closing brakcet.
            if char in mapping:
                # If stack is empty -> there's no opening bracket to match.
                # stack.pop() -> remove & return the most recent opening bracket
                # mapping[char] -> fetches the opening bracket(value) that should match this closing bracket(key).
                # If the popped character is not equal to the fetched opening bracket: return False.
                if not stack or stack.pop() != mapping[char]:
                    return False
            # If char is not an opening bracket it must be a closing bracket.
            else:
                stack.append(char)
        # since return type is bool: if the len(stack) is equal to 0 -> valid & False otherwise.
        return len(stack) == 0