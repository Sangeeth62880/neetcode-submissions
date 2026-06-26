class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = 0
        seen = {0:1}
        c = 0
        for i,n in enumerate(nums):
            pre += n
            if pre - k in seen:
                c += seen[pre-k]
            seen[pre] = seen.get(pre,0)+1
        return c