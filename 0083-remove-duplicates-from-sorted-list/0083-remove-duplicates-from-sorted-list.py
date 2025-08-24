# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Creating a current pointer and pointing it to the same node as head.
        curr = head

        '''
        This loop runs when both current and current.next exist.
        In the very last iteration curr.next.next will point to the null pointer of the LL.
        Also in the last iteration we have curr but we don't have curr.next & because of that 
        the while loop terminates.
        '''

        while curr and curr.next:
            # if current node's val & next node's val are equal:
            if curr.val == curr.next.val:
                # we skip over the next node by linking the next node
                # to the next subsequent node.
                curr.next = curr.next.next 
            # On the other hand if they're not equal:
            else:
                # We move as we usually do to the next pointer
                # since we want unique nodes in the final LL.
                curr = curr.next

        # We return the head of the LL without any duplicates.
        return head