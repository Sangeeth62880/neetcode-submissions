class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        max_left = 0
        max_right = 0
        result = 0
        while l <= r:
            if max_left <= max_right:
                max_left = max(max_left,height[l])
                result += max_left- height[l]
                l = l+1
            else:
                max_right = max(max_right,height[r])
                result += max_right - height[r]
                r = r - 1
        return result