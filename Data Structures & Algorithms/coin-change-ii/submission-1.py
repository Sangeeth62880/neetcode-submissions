class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        from functools import lru_cache
        n = len(coins)
        @lru_cache(None)
        def coin(n,s):
            if s == 0:
                return 1
            if n == 0:
                return 0
            if coins[n-1] <= s:
                return coin(n,s-coins[n-1]) + coin(n-1,s)
            else:
                return coin(n-1,s)
        return coin(n,amount)
        
        