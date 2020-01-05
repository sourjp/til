'''
Runtime: 28 ms, faster than 56.11% of Python3 online submissions for Climbing Stairs.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        i = 1
        
        while i < n:
            a, b = a+b, a
            i += 1
            
        return a