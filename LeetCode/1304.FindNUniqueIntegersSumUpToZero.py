''' https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
Runtime: 28 ms, faster than 83.69% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
'''

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1: return [0]
        
        if n % 2 == 0:
            ans = []
            for i in range(1, n//2+1): 
                ans.append(i)
                ans.append(-i)
        
        else:
            ans = [0]
            for i in range(1, n//2+1): 
                ans.append(i)
                ans.append(-i)
        
        return ans
            