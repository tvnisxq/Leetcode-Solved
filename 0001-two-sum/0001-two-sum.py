class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty dictionary to store numbers we seen so far with their 
        # index. {number: index}
        numMap = {}

        # Looping through the list nums. i is the current index and num the current 
        # number. Enumerate allows us to access both the index and the value at the 
        # same time. 
        for i, num in enumerate(nums):
            # Calculates the number we need to find so that num + complement = target.
            complement = target - num   # if target = 9 and num = 2, then complement = 7.

            # Check if the complement exists in our numMap.
            if complement in numMap:
                return[numMap[complement], i] # numMap[complement] gives the index of the complement, while i is the current index.

            # If no match was found, store the current number and it's index in the numMap for future reference. 
            numMap[num] = i
        
        # Safe net in case no pair is found.
        return [] # But this line is never executed as the problem states that one solution is guaranteed. 