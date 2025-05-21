class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_to_zero = set()
        cols_to_zero = set()
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if not matrix[i][j] and i not in rows_to_zero:
                    rows_to_zero.add(i)
                if not matrix[i][j] and j not in cols_to_zero:
                    cols_to_zero.add(j)
        
        for row in rows_to_zero:
            for j in range(cols):
                matrix[row][j] = 0
        for i in range(rows):
            for col in cols_to_zero:
                matrix[i][col] = 0
        
        return matrix
