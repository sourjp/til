class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximum = max(nums)
            
        for val in nums:
            if val == maximum:
                continue
            elif maximum < val*2:
                return -1
        
        return nums.index(maximum)
