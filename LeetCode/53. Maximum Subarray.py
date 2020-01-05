'''
Runtime: 84 ms, faster than 9.27% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.5 MB, less than 79.67% of Python3 online submissions for Maximum Subarray.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        merge = nums[0]
        ans = nums[0]
        
        for i in range(1, len(nums)):
            merge = max(nums[i], nums[i]+merge)
            ans = max(ans, merge)
            
        return ans