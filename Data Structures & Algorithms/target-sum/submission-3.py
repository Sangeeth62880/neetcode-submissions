class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        from functools import lru_cache
        total = sum(nums)
        n = len(nums)
        if (total+target) %2  != 0:
            return 0
        s1 = (total+target)//2
        @lru_cache(None)
        def target(n,s):
            if n == 0:
                return 1 if s == 0 else 0

            if nums[n-1] == 0:
                return 2 * target(n-1,s)
            if nums[n-1] <= s:
                return target(n-1,s-nums[n-1]) + target(n-1,s)
            else:
                return target(n-1,s)
        return target(n,s1)
