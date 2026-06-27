class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = float('-inf')
        curr = 0
        for i in range(len(nums)):
            if (nums[i]> nums[i]+curr):
                curr = nums[i]
            else:
                curr = nums[i] + curr 
            m = max(m,curr)
        return m