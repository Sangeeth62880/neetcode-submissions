class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        from functools import lru_cache
        total = sum(nums)
        if total % 2 != 0:
                return False
        n = len(nums)
        target = total//2
        @lru_cache(None)
        def subsum(n,s):
            if s == 0:
                return True
            if n == 0:
                return False
            if nums[n-1] <= target:
                return subsum(n-1,s - nums[n-1]) or subsum(n-1,s)
            else:
                return subsum(n-1,s)
        return subsum(n,target)

