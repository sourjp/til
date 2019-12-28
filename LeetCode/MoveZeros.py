''' https://leetcode.com/problems/move-zeroes/submissions/
Runtime: 52 ms, faster than 73.95% of Python3 online submissions for Move Zeroes.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Move Zeroes.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                zero_cnt += 1
        
        while zero_cnt > 0:
            nums.pop(0)
            nums.append(0)
            zero_cnt -= 1



''' https://leetcode.com/problems/move-zeroes/submissions/
Runtime: 48 ms, faster than 88.31% of Python3 online submissions for Move Zeroes.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Move Zeroes.
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        store = []
        zero_cnt = 0
        
        for i in nums:
            if i == 0:
                zero_cnt += 1
            else:
                store.append(i)
        
        store += [0 for _ in range(zero_cnt)]

        for i in range(len(nums)):
            nums[i] = store[i]
                