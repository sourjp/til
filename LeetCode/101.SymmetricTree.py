''' https://leetcode.com/problems/symmetric-tree/

Runtime: 36 ms, faster than 60.85% of Python3 online submissions for Symmetric Tree.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.

Solution1 is compare leftside and rightside one by one. The point is null object. So alternatively add False object.
Solution2 is more impressive way. Function doesn't make additional list , it just compare each value one by one.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if not root.left and not root.right:
            return True
        
        if not root.left or not root.right:
            return False
        
        queue = [root]
        bottom_of_tree = False
        
        while not bottom_of_tree:
            level_order = []
            cnt = 0
            
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node == False:
                    level_order.append(False)
                else:
                    level_order.append(node.val)
                    queue.append(node.left) if node.left else queue.append(False)
                    queue.append(node.right) if node.right else queue.append(False)
                    cnt += 1
            
            if cnt == 0:
                break
            elif cnt == 1:
                continue
            elif cnt % 2 == 1:
                return False
            else:
                n = len(level_order)//2
                ls = level_order[:n]
                rs = level_order[n:]
            
                for l, r in zip(ls, rs[::-1]):
                    if l != r:
                        return False
                
        return True

'''
Runtime: 32 ms, faster than 82.29% of Python3 online submissions for Symmetric Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.
'''

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def reverse(t1, t2):
            if not t1 and not t2:
                return True
            
            if not t1 or not t2:
                return False
            
            return t1.val == t2.val \
               and reverse(t1.left, t2.right) \
               and reverse(t1.right, t2.left)
                
        return reverse(root, root)
                    