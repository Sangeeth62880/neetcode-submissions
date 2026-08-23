class Solution:
    def rob(self, nums: List[int]) -> int:
        p2 = 0
        p1 = 0
        for m in nums:
            current = max(p1,p2+m)
            p2 = p1
            p1 = current
        return p1
