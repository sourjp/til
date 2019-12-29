''' https://leetcode.com/problems/diameter-of-binary-tree/submissions/
O(n), O(n)

Runtime: 44 ms, faster than 78.95% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Diameter of Binary Tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        
        def depth(node):
            if not node:
                return 0
            
            leftdepth = depth(node.left)
            rightdepth = depth(node.right)
            
            print(leftdepth, rightdepth)
            self.ans = max(self.ans, leftdepth + rightdepth)
            
            return max(leftdepth, rightdepth) + 1
        
        depth(root)
        
        return self.ans