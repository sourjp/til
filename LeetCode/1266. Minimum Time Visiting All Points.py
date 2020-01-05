''' https://leetcode.com/problems/minimum-time-visiting-all-points/submissions/
Runtime: 52 ms, faster than 95.30% of Python3 online submissions for Minimum Time Visiting All Points.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Minimum Time Visiting All Points.
'''
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        
        for i in range(1, len(points)):
            sx, sy = points[i-1]
            ex, ey = points[i]
            
            ans += max(abs(ex-sx), abs(ey-sy))
        
        return ans