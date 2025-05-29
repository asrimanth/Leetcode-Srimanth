# Time Complexity: O(M*N)
# Space Complexity: O(1)
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        result = 0
        m, n = len(board), len(board[0])
    
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    if i > 0 and board[i-1][j] == 'X':
                        continue # Part of a vertical ship
                    if j > 0 and board[i][j-1] == "X":
                        continue # Part of a horizontal ship
                    # Below implies start of a sequence
                    result += 1

        return result