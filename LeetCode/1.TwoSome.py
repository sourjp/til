''' https://leetcode.com/problems/two-sum/
Runtime: 280 ms, faster than 32.79% of Python3 online submissions for Two Sum.
Memory Usage: 13.7 MB, less than 86.51% of Python3 online submissions for Two Sum.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = []
        
        for i in range(len(nums)):
            want = target - nums[i]
            if want in memo:
                ans = [nums.index(want), i]
                return ans
            
            memo.append(nums[i])
        
        return False
    
