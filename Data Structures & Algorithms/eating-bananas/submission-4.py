class Solution:
    def minEatingSpeed(self, piles, h):
        from math import ceil
        l, r = 1, max(piles)
        result = max(piles)
        
        while l <= r:
            k = (l + r) // 2
            hours = sum(ceil(p / k) for p in piles)
            
            if hours <= h:
                result = k
                r = k - 1
            else:
                l = k + 1
        
        return result