''' https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
first solution is bottom-up. it is going to inclement value one by one, and compare left and right to choose maximum depth.
second solution is top-down as a recursiv ways. this is popler, but take care of how to count.

O(N), O(1)

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


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.ans = 0
        depth = 0
        
        def traverse(root, depth):
            if not root:
                self.ans = max(self.ans, depth)
                return
            
            traverse(root.left, depth + 1)
            traverse(root.right, depth + 1)
        
        traverse(root, depth)
        
        return self.ans        