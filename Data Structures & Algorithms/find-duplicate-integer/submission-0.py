class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = set()
        for i in nums:
            if i in freq:
                return i
            freq.add(i)
        return False