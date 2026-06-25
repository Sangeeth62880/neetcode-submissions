class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.rev(0,n-1,nums)
        self.rev(0,k-1,nums)
        self.rev(k,n-1,nums)

    def rev(self,l,r,nums):
            while l<r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1