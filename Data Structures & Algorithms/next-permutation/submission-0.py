class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        piv = -1
        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                piv = i
                break
        
        if (piv == -1):
            return nums.reverse()
        
        for j in range(n-1,piv,-1):
            if nums[j] > nums[piv]:
                nums[j],nums[piv] = nums[piv],nums[j]
                break
        nums[piv+1:] = nums[piv+1:][::-1]
        return nums[piv+1:]