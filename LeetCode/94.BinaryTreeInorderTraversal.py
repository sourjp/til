''' https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/, https://leetcode.com/problems/binary-tree-inorder-traversal/
if you want to take the stack way.
it must be start from maximum depth of left side.
so before poping from stack, stack have to has whole of left side. 

O(N), O(N)

Runtime: 28 ms, faster than 81.46% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        ans = []
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
            
            return 
        
        inorder(root)
        
        return ans
        
