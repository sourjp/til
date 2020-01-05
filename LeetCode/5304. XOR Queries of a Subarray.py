class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        p = [0]
        
        for val in arr:
            p.append(p[-1] ^ val)
        
        ans = []
        for query in queries:
            x, y = query
            ans.append(p[x] ^ p[y+1])
        
        return ans

'''
class Solution:
    def xorQueries(self, arr, queries) -> list:
        ans = []
        
        for query in queries:
            s, e = query
            result = arr[s]
            s += 1

            while s <= e:
                result = result ^ arr[s]
                s += 1
                
            print(result)
            ans.append(result)
            
        return ans
'''

arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]

arr2 = [4,8,2,10]
queries2 = [[2,3],[1,3],[0,0],[0,3]]

s = Solution()
print(s.xorQueries(arr, queries))
print(s.xorQueries(arr2, queries2))