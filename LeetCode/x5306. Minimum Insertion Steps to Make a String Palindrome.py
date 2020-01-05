from functools import lru_cache

class Solution:
    def minInsertions(self, s: str) -> int:
        INF = float('inf')
        
        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return INF
            elif i == j:
                return 0
            elif i == j-1:
                return +(s[i] != s[j])
            elif s[i] == s[j]:
                return dp(i+1, j-1)
            else:
                return min(dp(i, j-1), dp(i+1, j)) + 1
        return dp(0, len(s) - 1)

'''
class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)
        if length == 1:
            return 0
        
        cnt = 0
        if length % 2 == 0:
            front = s[:length//2]
            after1 = s[length//2:]
            after2 = after1[::-1]

            print(front, after2)
            
            for i in range(length//2):
                if front[i] not in after2:
                    cnt += 1
                    
        elif length % 2 == 1:
            front = s[:length//2]
            after1 = s[length//2+1:]
            after2 = after1[::-1]

            print(front, after2)
            
            for i in range(length//2):
                if front[i] != after2[i]:
                    cnt += 1
        
        return cnt
'''

s = "leetcode"
sol = Solution()
print(sol.minInsertions(s))