''' https://leetcode.com/problems/non-decreasing-array/submissions/
Runtime: 192 ms, faster than 93.71% of Python3 online submissions for Non-decreasing Array.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Non-decreasing Array.
'''
class Solution:
    def checkPossibility(self, nums) -> bool:
        twice_checker = False

        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if twice_checker:
                    return False

                twice_checker = True
                
                if i > 1 and nums[i] <= nums[i-2]:
                    nums[i] = nums[i-1]
                 
        return True

pro1 = [3, 4, 2, 3]
pro2 = [2, 3, 3, 2, 4]
pro3 = [-1, 4, 2, 3]

s = Solution()
print(s.checkPossibility(pro1))
print(s.checkPossibility(pro2))
print(s.checkPossibility(pro3))
