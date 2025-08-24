# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
            Converting the linked list to array:
            ▷ Time: O(n) -> 
            ▷ Space: O(n) -> 
        '''
        # Create an empty list to store LL nodes
        nums = []

        while head:
            nums.append(head.val) # Append single node per iteration 
            head= head.next # Move the head pointer to the next node.

        # Initializing two pointers: left(l) starting from beginning and right(r) starting from end.
        l, r = 0, len(nums) - 1
        # Loop runs till the left pointer's index is less than or equal to right pointer's index.

        while l <= r:
            # If the value stored in list at the index of left pointer 
            # is not equal to that of left pointer -> CAN'T BE A PALINDROME. 

            if nums[l] != nums[r]: 
                return False # Hence return False

            # Else increment the pointer's position    
            l += 1
            r -= 1

        # Return True if the entire loop has finished executing and no anomalies we're found
        return True
        