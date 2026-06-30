class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = nums[0]
        m2 = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            candidates = [nums[i],m1*nums[i],m2*nums[i]]
            m1 = max(candidates)
            m2 = min(candidates)
            res = max(res,m1)
        return res