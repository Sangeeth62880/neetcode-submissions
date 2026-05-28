class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from functools import lru_cache
        n = len(coins)
        @lru_cache(None)
        
        def coin(n,s):

            if s == 0:
                return 0
            if n == 0:
                return float('inf')

            if coins[n-1] <= s:
                return min(1+coin(n,s-coins[n-1]),coin(n-1,s))
            else:
                return coin(n-1,s)
        
        res = coin(n,amount)
        if res != float('inf'):
            return res
        else:
            return -1
            
