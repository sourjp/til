''' https://leetcode.com/problems/single-number/submissions/
Runtime: 68 ms, faster than 99.99% of Python3 online submissions for Single Number.
Memory Usage: 15.3 MB, less than 8.20% of Python3 online submissions for Single Number.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i-1]:
                return nums[i-1]
            
        return nums[-1]
