'''
Runtime: 48 ms, faster than 15.06% of Python3 online submissions for Reverse Linked List.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Reverse Linked List.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev = None
        curr = head

        while curr:
            nextnode = curr.next    # store next pointer
            curr.next = prev    # change pointer right to left
            prev = curr # store pointer to change right to left for next trun
            curr = nextnode # try next pointer
            
        return prev