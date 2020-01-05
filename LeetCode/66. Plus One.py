# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''.join(map(str, digits))
        number = int(number) + 1

        ans = [int(val) for val in str(number)]
        return ans