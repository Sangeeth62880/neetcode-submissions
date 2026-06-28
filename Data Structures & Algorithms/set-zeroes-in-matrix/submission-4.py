class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        c = any(matrix[i][0] == 0 for i in range(len(matrix)))
        r = any(matrix[0][j] == 0 for j in range(len(matrix[0])))

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if c:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if r:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
