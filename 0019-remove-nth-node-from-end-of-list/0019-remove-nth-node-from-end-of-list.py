# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Time: O(M); where M is the size of the linked list.
        Space: O(1); we're really just using a few variables/pointers.
        """
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy

        for _ in range(n+1):
            ahead = ahead.next
        while ahead:
            ahead = ahead.next
            behind = behind.next
        behind.next = behind.next.next
        return dummy.next

