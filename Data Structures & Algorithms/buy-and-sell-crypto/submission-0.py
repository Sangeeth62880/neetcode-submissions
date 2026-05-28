class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        maxprofit = 0
        for p in prices:
            if min > p:
                min = p
            profit = p - min
            if maxprofit < profit:
                maxprofit = profit
        return maxprofit