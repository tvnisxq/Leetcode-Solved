# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Handling edge cases: -> return None if the list is empty or None
        if len(lists) == 0:
            return None

        # Divide Part: Keep reducing the elements until 
        # the "reduced lists" are single element/node lists.
        while len(lists) > 1:
            # Temporary storage to storre merged results from current round.
            # Gets reset after each iteration.
            final_merged = []

            # This range gives 0, 2, 4 , 6(even indices)
            # jump by 2 to pair up adjacent.
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                '''
                    This logic for creating l2 deals with the case where 
                    "number of list" in lists is Odd. In "Odd number of list",
                    the last list left is unpaired.
                '''
                # It's ok if the last unpaired element returns None, bcoz 
                # its already a list with single element. 
                l2 = lists[i+1] if (i+1) < len(lists) else None
                 
                # Calls the helper function mergeLists.
                final_merged.append(self.mergeLists(l1, l2)) # merge the pair and append the final result to temporary storage
            
            # Update: replace original list with merged results.
            # This halves the number of lists each round.
            lists = final_merged

        # After the loop only one list remains -> return it.
        return lists[0]

    '''
        Helper Function:
        ▷ Purpose: Merge two sorted linked lists.
        ▷ Parameters: two linked list heads. Can be None as well.
    '''
    def mergeLists(self, l1, l2):
        '''
            Dummy Node Trick: creates a placeholder to simplify logic
            ▷ Tail points to the last node in our result list.
            This avoids special handling for the first node.
        '''
        dummy = ListNode()
        tail = dummy 

        # Main merge loop:
        '''
        continue while both lists have nodes. 
        We exit when one becomes None.
        '''
        while l1 and l2:
            '''
                • choose the smaller value.
                • link it to our result.
                • move the chosen pointer forward.
            '''
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            # move tail to the newly added node.            
            tail = tail.next

        '''
            Attach Remaining: One list might have leftover nodes.
            Since lists are sorted, we can attach the entire remaining position
        '''
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        # Skip dummy: return the actual head(skip the dummy placeholder)
        return dummy.next