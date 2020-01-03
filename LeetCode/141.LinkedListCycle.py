''' https://leetcode.com/problems/linked-list-cycle/submissions/
O(N), O(N)

Runtime: 68 ms, faster than 10.70% of Python3 online submissions for Linked List Cycle.
Memory Usage: 16.4 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.

Solution 1 compare the memory cell, because it has same loops, it means tail refer same memory cell. so use id(). the point is 'head', not 'head.val'. because head.val is just value but head is object. so it should compare the object. it means 'head'.
Solution 2 also O(N) but space is O(1). The trick is slow and fast. slow = n but fast = 2n then fast and slow would meet same position even the loop as even or odd.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        has_seen = set()
        
        while head:
            if id(head) in has_seen:
                return True
            
            else:
                has_seen.add(id(head))
                
            head = head.next
            
        return False

'''
Runtime: 44 ms, faster than 91.38% of Python3 online submissions for Linked List Cycle.
Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while id(slow) != id(fast):
            if not fast or not fast.next:
                return False
            
            slow = slow.next
            fast = fast.next.next
            
        return True