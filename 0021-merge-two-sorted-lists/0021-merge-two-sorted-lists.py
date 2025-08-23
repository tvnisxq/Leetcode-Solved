# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            In-place Modifications:
            -> refers to modifying the structure or data within existing nodes without allocating
            new memory for new nodes. Typically involves re-arranging pointers or updating data fields
            within current nodes.   
        '''

        # Creates a new dummy node(often called dummy head). Its job is to simplify 
        # handling the head of the merged list.
        dummy = ListNode()

        # sets the tail pointer to the dummy. Tail will always point to the last node of the merged lists
        # as we build it. Initially merged list is empty so tail is the dummy.
        tail = dummy

        # This loop continues while both the lists are non-empty. Each iteration picks the smaller 
        # of the two front nodes & appends it to the merged list.
        while list1 and list2:
            
            # compares the current values of the lists
                # If list1 has the smaller value.
            if list1.val < list2.val:

                tail.next = list1 # attaches the current list node to the merged list
                list1 = list1.next # advances list1 node to it's next node(we consumed that node)

            else: # if list2 has the smaller value.

                tail.next = list2
                list2 = list2.next

            # advances the tail pointer to the node we just attached, keeping it at the end of the merged list.
            tail = tail.next 

        '''
            After the while loop atleast one list is exhausted(becomes None). The other list
            (if non-empty), since has it's nodes sorted so we can attach them directly.
        '''
        # If list1 is non-empty
        if list1:
            tail.next = list1 # links the leftover nodes at the end of the merged list

        # If list2 is non-empty
        elif list2:
            tail.next = list2

        # dummy.next is the head of the merged list(the node after the dummy).
        # Return that as merged result.
        return dummy.next 

        '''
            ▷ TIME: If n is the length of the list1 & m is the length of the list2, total number 
            number of operations inside the loop is atmost n+m. -> O(n+m).

            ▷ SPACE: The space complexity is constant because the algorithm modifies the nodes
            in-place instead of creating new nodes. Just uses constant amount of extra memory for pointers 
            like dummy, tail, list1, list2. Space occupied by these pointers doesn't grow with input size.
            -> O(1). 
        '''
        