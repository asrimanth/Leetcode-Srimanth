class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_locs = set()
        col_locs = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    row_locs.add(i)
                    col_locs.add(j)

        for row in row_locs:
            matrix[row] = [0] * n
        for col in col_locs:
            for i in range(m):
                matrix[i][col] = 0

        return matrix
        