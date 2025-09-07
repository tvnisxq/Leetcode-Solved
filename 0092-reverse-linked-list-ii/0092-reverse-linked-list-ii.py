# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Time: O(n); we're really just iterating through the list only once.
        Space: O(1); we're only using some pointers and no other data structure.
        """
        """Initialisation"""
        # Initializig a Dummy Node with val=0 pointing at head 
        dummy = ListNode(0, head)

        # Creating two pointers previous and current
        leftPrev, curr = dummy, head
        for i in range(left - 1):
            leftPrev, curr = curr, curr.next
        
        """ Delniking -> Reverse from left to right"""
        # Now curr = "left" and leftPrev = "Node before left"

        prev = None
        for i in range(right - left + 1):
            tmpCurr = curr.next
            curr.next = prev
            prev, curr = curr, tmpCurr
        
        """ Relinking"""
        leftPrev.next.next = curr # Curr is the node after "right".
        leftPrev.next = prev  # Prev is "right".

        return dummy.next
