class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
            Two Pointers Method(optimal):
        '''
        n = len(numbers)    
        left = 0
        right = n - 1
        
        # Loop runs until the left & right pointer merge at a common index:
        while left < right:
            # sum equals the number at right pointer plus the number at left pointer
            sum = numbers[left] + numbers[right] 

            if sum == target:
                '''
                 return list of indices of pointers in just right next
                to the current position of the pointer -> 1-indexed array
                '''
                return [left+1, right+1]
            
            # Move the left pointer ahead becoz in a ascending-sorted list,
            # as we move from left to right the values start inceasing. 
            elif sum < target:
                left += 1 
            
            # Otherwise if the sum is more than the target we must reduce
            # the values of the number so we right to left in an ascending-sorted list.
            else:
                right -= 1