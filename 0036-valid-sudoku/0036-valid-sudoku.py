# Time Complexity: O(N^2) = O(81) = O(1)
# Space Complexity: O(3 * N^2) = O(3 * 9 * 9) = O(243)
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n_rows = len(board)
        n_cols = len(board[0])
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(n_rows):
            for j in range(n_cols):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[(i//3, j//3)]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[(i//3, j//3)].add(board[i][j])
        return True
