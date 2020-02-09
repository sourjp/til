''' https://leetcode.com/problems/two-sum/
Runtime: 292 ms, faster than 30.44% of Python3 online submissions for Two Sum.
Memory Usage: 13.7 MB, less than 79.07% of Python3 online submissions for Two Sum.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = []
        
        for i in range(len(nums)):
            want = target-nums[i]
            if nums[i] in memo:
                return [nums.index(want), i]
            
            memo.append(want)
        
        return False

'''
untime: 40 ms, faster than 97.99% of Python3 online submissions for Two Sum.
Memory Usage: 14.1 MB, less than 62.56% of Python3 online submissions for Two Sum.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i in range(len(nums)):
            want = target-nums[i]
            if want in memo: return [memo[want], i]
            memo[nums[i]] = i
        return False