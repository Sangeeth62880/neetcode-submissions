class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        rows = len(matrix)
        col = len(matrix[0])
        r = rows * col -1
        while l<=r:
            m = (l+r)//2
            rows = m//col
            cols = m%col
            if matrix[rows][cols] == target:
                return True
            elif matrix[rows][cols] < target:
                l = m+1
            else:
                r = m-1
        return False