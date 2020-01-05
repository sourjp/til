''' https://leetcode.com/problems/find-numbers-with-even-number-of-digits/submissions/
Runtime: 48 ms, faster than 90.71% of Python3 online submissions for Find Numbers with Even Number of Digits.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.
'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
            
        for line in nums:
            if len(str(line)) % 2 == 0:
                ans += 1
                
        
        return ans