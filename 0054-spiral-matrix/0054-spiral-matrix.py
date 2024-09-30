# Time Complexity: O(M * N)
# Space Complexity: O(1) excluding result
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        if not matrix:
            return []
        result = []
        max_level = m - 1

        row_start, row_end = 0, m-1
        col_start, col_end = 0, n-1

        while len(result) < m * n:
            # l -> r
            for j in range(col_start, col_end+1):
                result.append(matrix[row_start][j])
            row_start += 1
            # r -> down
            for i in range(row_start, row_end+1):
                result.append(matrix[i][col_end])
            col_end -= 1

            # down -> l1
            if row_start <= row_end:
                for j in range(col_end, col_start-1, -1):
                    result.append(matrix[row_end][j])
                row_end -= 1

            # l1 -> up
            if col_start <= col_end:
                for i in range(row_end, row_start-1, -1):
                    result.append(matrix[i][col_start])
                col_start += 1
        return result
