''' https://leetcode.com/problems/merge-two-binary-trees/submissions/
Runtime: 80 ms, faster than 76.46% of Python3 online submissions for Merge Two Binary Trees.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Merge Two Binary Trees.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return
        elif t1 and not t2:
            return t1
        elif t2 and not t1:
            return t2
        
        merge = TreeNode(t1.val + t2.val)
        
        merge.left = self.mergeTrees(t1.left, t2.left)
        merge.right = self.mergeTrees(t1.right, t2.right)
        
        return merge
        