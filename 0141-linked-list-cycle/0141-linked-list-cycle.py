# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
            Floyd Cycle Algorithm:
            ▷ also called as the fast & slow pointer algorithm/pattern.
            ▷ sometimes even referenced as the hare & tortoise algorithm/pattern.
            ▷ efficient in terms of Memory: O(1) constant space.
            ▷ the fast & slow pointers are at SOME POINT, MOST CERTAINLY going to point to the same node.
        '''
        # Creating a dummy node in the LL.
        dummy = ListNode()
        # pointing in to the head of the LL.
        dummy.next = head
        # taking two pointers: fast & slow and setting them to the dummy node.
        slow = fast = dummy

        '''
        While loop traversal:
        the slow pointer moves one step each iteration and the fast pointer moves 
        two steps each iteration. The conditon being presence of both node of the 
        fast pointer & its next subesquent node is because next node must also be 
        present in order to move the fast pouinter by 2 steps. 
        '''
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            # If fast and slow pointers merge in the same node,
            # there must be a cycle in the LL.
            if fast is slow:
                # Hence return True
                return True
        # return False otherwise
        return False