'''
Forward scan with Look ahead:                                             | • Requires boundary
• Look ahead to check if current character should be added or subtracted. |   checking (i< n-1).
• Clean logic and easy to understand.                                     | • Two different    
• Handles subtraction cases explicitly.                                   |   increments(i +=1) V/s 
• Good solution to start with in a Live Interview.                        |   (i += 2).
                                                                                    
'''                                                                        
class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dict of Romans: Values as Key: Value pairs.
        dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M':1000}
        
        # Initialize sum as 0. This will store out result.
        sum = 0
        n = len(s)

        # This is used to track iterations and corresponding operations.
        i = 0
        
        while i < n:
            # Check if the current character is smaller than next(subtraction case).
            if i < n-1 and dict_roman[s[i]] < dict_roman[s[i+1]]:
                sum += dict_roman[s[i+1]] - dict_roman[s[i]] # sum = next - current
                i += 2 # skip both the characters.

            # code is here means: current char> next 
            else:
                sum += dict_roman[s[i]] # simply add it up to sum.
                i += 1
        return sum

'''
    Reverse Scan Approach:
    • ELegant approach
    • After the first approach, one should optimize the solution for this(if asked & time permits).
    • Cleaner logic and no look ahead needed, single increment and no boundary checks. 
'''

class Solution:
    def romanToInt(self, s: str) -> int:

        dict_roman = {
            'I': 1, 'V': 5, "X": 10,
            'L': 50, 'C': 100, 'D': 500, 
            'M': 1000 
        }

        result = 0
        prev_value = 0 # value of the characters we processed previously.

        # Scan from right to left(End -> beginning)
        # starts from last index, stops right before index -1 i.e at 0
        # and decrements by -1.
        for i in range(len(s)-1, -1, -1):  
            current_value = dict_roman[s[i]] # fetches the value of roman numeral

            # Logic: if current val is smaller than the previous one, it means 
            # this character is to be subtracted from prev.
            if current_value < prev_value: # For 1st iteration: prev_value = 0 means this if condition is false.
                result -= current_value

            else:
                result += current_value

            prev_value = current_value # update the prev_value to become the current value.
        
        return result
