class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
        Brute Force Approach:
        '''
        # Check if the lengths of both strings are equal
        if len(s) != len(t): # two strings can be anagrams only if they are of equal lengths.
            return False     # return False if they are not.
        
        '''
            TIME:
            The return type is given as bool.
            So if the conditon that sorted strings are equal is satisfied, True is returned and False otherwise.
            Python's sorted function uses Timsort -> a derivation of merge and insertion sort combined which has a worst 
            case time complexity of O(N log N), where N=len(string). So total = O(N log N + M log M).
            But since the strings are of equal lengths(initial check) -> O(N log N).

            After sorting comparison of two sorted lists is taking place O(N). However this is 
            dominated by sorting step SO OVERALL TIME COMPLEXITY DOESN'T CHANGE.

            SPACE:
            Sorted function in python returns a new list with sorted elements. Requires additional space to store 
            these new lists. Timsort has a worst case space complexity of O(N). But here two strings are being sorted 
            so it becomes O(N + M). Since the strings here are of same length -> O(N)
        '''   
        return sorted(s) == sorted(t) 