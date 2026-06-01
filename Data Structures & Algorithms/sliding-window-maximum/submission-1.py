class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        a = []
        dq = deque()
        for r in range(len(nums)):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            if dq[0] < l:
                dq.popleft()
            if r-l+1 == k:
                a.append(nums[dq[0]])
                l+=1
        return a
