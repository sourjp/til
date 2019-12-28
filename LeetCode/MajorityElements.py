''' https://leetcode.com/problems/majority-element/submissions/
O(n), O(n/2)

Runtime: 184 ms, faster than 71.98% of Python3 online submissions for Majority Element.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Majority Element.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mark_dict = {}
        for k in nums:
            if not k in mark_dict:
                mark_dict[k] = 1
            else:
                mark_dict[k] += 1
                
        k, v = max(mark_dict.items(), key=lambda x: x[1])
        return k
        

'''
O(nlogn), O(1)

Runtime: 168 ms, faster than 97.19% of Python3 online submissions for Majority Element.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Majority Element.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        
        return nums[len(nums)//2]

'''
O(nlogn), O(1) 

Runtime: 176 ms, faster than 86.80% of Python3 online submissions for Majority Element.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Majority Element.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        
        cnt = 1
        max_key = nums[0]
        max_log = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                cnt += 1
            else:
                if cnt > max_log:
                    max_key = nums[i]
                    max_log = cnt
                    cnt = 1
   
        if cnt > max_log:
            max_key = nums[i]
            cnt = 1
            
        return max_key
