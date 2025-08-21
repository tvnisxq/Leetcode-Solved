# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
            Iterative Solution(Using Two Pointers):
                ▷ Time: O(n)
                ▷ Space: O(1)
        '''
        # Initialising the pointers.
        prev, curr = None, head

        # Looping through the Linked List.
        while curr:
            nxt = curr.next # temporary variable to keep track of original links.
            curr.next = prev # pointing the nodes to prev instead of next(reversal).
            prev = curr # shifting the prev pointer to the curr position.
            curr = nxt # moving the traversal pointer one step forward in original linked list.

        # prev is returned as the head of the newly reversed list. 
        return prev 