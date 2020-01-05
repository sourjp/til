# https://leetcode.com/problems/find-pivot-index/

class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        maximum = sum(nums)
        left = 0
        
        for i, val in enumerate(nums):
            if left == (maximum - left - nums[i]):
                return i
            
            left += val
            
        return -1