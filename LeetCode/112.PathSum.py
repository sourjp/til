''' https://leetcode.com/problems/path-sum/submissions/
Runtime: 36 ms, faster than 96.45% of Python3 online submissions for Path Sum.
Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Path Sum.
'''
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)