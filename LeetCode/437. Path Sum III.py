''' https://leetcode.com/problems/path-sum-iii/submissions/
Runtime: 832 ms, faster than 34.93% of Python3 online submissions for Path Sum III.
Memory Usage: 13.5 MB, less than 97.73% of Python3 online submissions for Path Sum III.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    def dfs(self, root, sum):
        if not root:
            return 0
        
        sum -= root.val
        
        result = 0
        if sum == 0:
            result = 1
            
        result += self.dfs(root.left, sum)
        result += self.dfs(root.right, sum)
        
        return result
        