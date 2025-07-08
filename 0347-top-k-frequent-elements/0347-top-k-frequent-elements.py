class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Creating a counter to store the freq:num as key:val pairs.
        freq_map = Counter(nums)
        # Creating a frequency bucket which is basically list of lists to house our elements.
        # the elements with highest frequency will be stored in the list of 
        # last position of the main list and then we'll negatively iterate for other elements.
        bucket = [[] for _ in range(len(nums)+1)]
        '''
            This line creates one extra empty list than the size of nums:
            because since if len(nums) = 6 this loop creates 6 empty lists but there will be 
            no elements in the nums which will occur 0 times. So we create one extra list for the worst case:
            If All elements are same: example: nums=[1,1,1,1,1] & k=2:
                    bucket becomes: [[],[],[],[],[]] (5 buckets with last bucket storing freq = 4 elements)
                    but since 1 is occuring 5 times it must be stored in bucket 5. Therefore: range is len   
                    (nums) + 1. 

        '''
        # Put numbers in appropriate buckets:
        for num,freq in freq_map.items():
            bucket[freq].append(num) # if an element occurs twice, we put it in bucket[2].

        # Initialising an empty list 'result' for storing the answer list.
        result = []

        # starts from highest frequenct in 'list' bucket and goes till 1(since end index in excluded in 
        # this syntax). -1 means we traverse backwards during the loop(from high to low frequency).
        for i in range(len(bucket)-1, 0, -1):
            # Since each bucket might contain multiple numbers
            for num in bucket[i]:
                # Adding the num in result list.
                result.append(num)
                # Stop as soon as we have k elements. This is an optimization.
                # We don't need to process all elements.
                if len(result) == k:
                    return result
        # In case we need fewer than k elements(edge case).
        return result

# Time: O(n) -> Linear scan to count, bucket fill, and collect result.
# Space: O(n) -> Counter + bucket list hold at most n elements.
