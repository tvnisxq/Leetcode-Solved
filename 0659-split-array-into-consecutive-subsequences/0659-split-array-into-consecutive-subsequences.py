from collections import Counter, defaultdict
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Freq tracks how many times the number is available to use0
        freq = Counter(nums)
        
        # appendFreq: tracks how many subsequences are waiting to append
        # a specific number as their next element. Key: number, Value:
        # count of subsequences subsequences ending at(number - 1)
        appendFreq = defaultdict(int)
        for num in nums:
        # Skip this number if it's already been used up
            if freq[num] == 0:
                continue 
            
            # GREEDY Choice 1: Try to append an existing subsequence. 
            # Check if there's a subsequence ending with (num-1) which needs num.
            if appendFreq[num] > 0:
                # Extend an existing subsequence
                appendFreq[num] -= 1    # One less subsequence waiting for num
                appendFreq[num+1] += 1  # Now it's waiting for num+1
                freq[num] -= 1          # Mark this number as used


            # GREEDY Choice 2: Start a new subsequence.
            # We need atleast num, num+1, num+2 to start a valid subsequence

            elif freq[num] > 0 and freq[num+1] > 0 and freq[num+2] > 0:
                # Start a new subsequence [num, num+1, num+2]
                freq[num] -= 1   
                freq[num+1] -= 1   
                freq[num+2] -= 1
                # This new subsequence is now waiting for num+3
                appendFreq[num+3] += 1
            
            # IF neither of the options work, we can't split the array validly
            else:
                return False

        return True