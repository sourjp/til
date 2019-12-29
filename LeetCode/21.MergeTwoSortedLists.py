''' https://leetcode.com/problems/merge-two-sorted-lists/submissions/
O(2N), O(1)

Runtime: 36 ms, faster than 75.45% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.

b-l2: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
b-l1: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
b-l1: ListNode{val: 2, next: ListNode{val: 4, next: None}}
b-l2: ListNode{val: 3, next: ListNode{val: 4, next: None}}
b-l2: ListNode{val: 4, next: None}

a-l2: ListNode{val: 4, next: ListNode{val: 4, next: None}}
a-l2: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 4, next: None}}}
a-l1: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 4, next: None}}}}
a-l1: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 4, next: None}}}}}
a-l2: ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 4, next: None}}}}}}
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
        