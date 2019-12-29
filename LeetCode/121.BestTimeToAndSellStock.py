''' https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
O(n), O(1)

Runtime: 56 ms, faster than 97.20% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.9 MB, less than 90.80% of Python3 online submissions for Best Time to Buy and Sell Stock.

1 7 7 0
2 1 1 0
3 1 5 4
4 1 5 4
5 1 6 5
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        maxnum = prices[0]
        minnum = prices[0]
        cnt = 1
        
        while cnt < len(prices):
            #print(cnt, minnum, maxnum, profit)
            if prices[cnt] < minnum:
                maxnum = prices[cnt]
                minnum = prices[cnt]

            else:
                if prices[cnt] > maxnum:
                    maxnum = prices[cnt]
            
            if profit < maxnum - minnum:
                profit = maxnum - minnum
                                    
            cnt += 1
        
        return profit

'''
short version.

Runtime: 56 ms, faster than 97.20% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.8 MB, less than 90.80% of Python3 online submissions for Best Time to Buy and Sell Stock.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        minnum = prices[0]
        cnt = 1
        
        while cnt < len(prices):
            if prices[cnt] < minnum:
                minnum = prices[cnt]

            else:
                profit = max(profit, prices[cnt] - minnum)

            cnt += 1
        
        return profit



''' TLE
O(n^2) // O(n * (n-1)/2), O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            cost = prices[i]
            getMax = max(prices[i+1:])
            
            if cost < getMax and profit < getMax - cost:
                profit = getMax - cost
    
        return profit