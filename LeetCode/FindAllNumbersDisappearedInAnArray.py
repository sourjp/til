''' https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/
O(n + n), O(1)

Runtime: 400 ms, faster than 59.90% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 20.5 MB, less than 46.43% of Python3 online submissions for Find All Numbers Disappeared in an Array.

[4, 3, 2, -7, 8, 2, 3, 1]
[4, 3, -2, -7, 8, 2, 3, 1]
[4, -3, -2, -7, 8, 2, 3, 1]
[4, -3, -2, -7, 8, 2, -3, 1]
[4, -3, -2, -7, 8, 2, -3, -1]
[4, -3, -2, -7, 8, 2, -3, -1]
[4, -3, -2, -7, 8, 2, -3, -1]
[-4, -3, -2, -7, 8, 2, -3, -1]
[-4, -3, -2, -7, 8, 2, -3, -1]
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n) - 1 # take index
            nums[i] = -abs(nums[i]) # change number to minus
        
        ans = []
        for i, v in enumerate(nums):
            if v > 0:
                ans.append(i+1)
        
        return ans



''' https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/
O(n), O(n)
Runtime: 376 ms, faster than 81.52% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 23.9 MB, less than 7.14% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        full_list = set([int(i) for i in range(1, len(nums)+1)])
        
        return full_list - set(nums)


''' https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/
O(n + n), O(n)

Runtime: 360 ms, faster than 94.25% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 19.8 MB, less than 46.43% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        memo = [0] * (len(nums))
        for i in nums:
            memo[i-1] += 1
        
        ans =[]
        for i in range(len(nums)):
            if memo[i] == 0:
                ans.append(i+1)
        
        return ans