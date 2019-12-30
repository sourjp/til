''' https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/, https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/
The solution1 have a trick by cc and nc. The cc count how many numbers are in same level. and The nc count how many numbers are in next level.
When cc count has finished, nc will switch to cc as next level counter.

The soultion2 is not count it. The same level operations has done in for loop. so Next level queue will be put in iterative argument.

O(n), O(n)

Runtime: 32 ms, faster than 85.80% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = [root]
        save = []
        
        cc = 1
        nc = 0
        
        while queue:
            node = queue.pop(0)
            save.append(node.val)
            cc -= 1
            
            if node.left:
                queue.append(node.left)
                nc += 1
                
            if node.right:
                queue.append(node.right)
                nc += 1
            
            if cc == 0:
                ans.append(save)
                save = []
                cc, nc = nc, cc
                
        return ans




class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        ans = []
        queue = [root]
        
        while  0 < len(queue):
            level_result = []
            
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_result.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
            ans.append(level_result)
            
        return ans
                
                