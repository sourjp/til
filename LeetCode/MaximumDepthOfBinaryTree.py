''' https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
Runtime: 28 ms, faster than 99.72% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 14.4 MB, less than 96.87% of Python3 online submissions for Maximum Depth of Binary Tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
                        
        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1

        return max(left_depth, right_depth)