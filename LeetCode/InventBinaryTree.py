''' https://leetcode.com/problems/invert-binary-tree/
Runtime: 44 ms, faster than 6.12% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Invert Binary Tree.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        root.left, root.right = root.right, root.left

        return root
        
