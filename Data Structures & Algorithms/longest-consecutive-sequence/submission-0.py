class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            if not nums:
                return 0
            nums = sorted(set(nums))
            l = 1
            c = 1
            for i in range(1,len(nums)):
                if nums[i] == nums[i-1] + 1:
                    c+=1
                else:
                    l=max(l,c)
                    c = 1
            return max(l,c)





