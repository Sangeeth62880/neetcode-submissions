class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        max_a = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = stack.pop() 
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                area = heights[h] * w
                max_a = max(max_a,area)
            stack.append(i)

        while stack:
            h = stack.pop()
            if not stack:
                w = len(heights)
            else:
                w = len(heights) - stack[-1] - 1

            area = heights[h] * w
            max_a = max(max_a, area)
        
        return max_a