''' https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/, https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/
Second solution is faster than first solution.
The unique points is stack root.right before left.right.
because stack is LIFO, so left one should be out side to achive pre-order.

O(N), O(N)

Runtime: 28 ms, faster than 81.39% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        ans = []
        
        def preorder(root) -> List[int]:
            if not root:
                return
        
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)
            
            return
        
        preorder(root)
        
        return ans
        

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        ans = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            ans.append(node.val)
            
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
                
        return ans
        