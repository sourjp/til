''' https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/, https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/
Postorder can soleve by stack way. because postorder traverse obosit of preorder.
it means the result of postorder is just reversed by peorder.
so take same implementation, but let answer reverse list.

O(N), O(N)

Runtime: 44 ms, faster than 5.63% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Postorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        
        def postorder(root):
            if not root:
                return
            
            postorder(root.left)
            postorder(root.right)
            
            ans.append(root.val)
            
            return

        postorder(root)
        
        return ans


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        ans = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            ans.append(node.val)
            
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        
        return ans[::-1]