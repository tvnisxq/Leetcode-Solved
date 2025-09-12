# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Iterative Solution(Two Pointers)"""
        # Time: O(n)
        # Space: O(1)

        # initializing the pointers
        prev, curr = None, head     # prev is None & curr points to head

        # Looping through the list
        while curr:
            nxt = curr.next # For keeping the original links
            curr.next = prev # Pointing the nodes to prev instead of next(reversal)
            prev = curr # Moving the current pointer to current position
            curr = nxt # Moving the traversal pointer one step forward in original LL.
        return prev # Prev is returned as the head of the newly reversed list.
