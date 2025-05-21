# Time Complexity: O(M*N)
# Space Complexity: O(M+N)
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
                if not matrix[i][j]:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        # for row in rows_to_zero:
        #     for j in range(cols):
        #         matrix[row][j] = 0
        # for i in range(rows):
        #     for col in cols_to_zero:
        #         matrix[i][col] = 0

        # Simplified below
        for i in range(rows):
            for j in range(cols):
                if i in rows_to_zero or j in cols_to_zero:
                    matrix[i][j] = 0

        return matrix
