

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_servers, col_servers = [0]*rows, [0]*cols
        for row in range(rows):
            for col in range(cols):
                row_servers[row] += grid[row][col]
                col_servers[col] += grid[row][col]
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] and (row_servers[i] > 1 or col_servers[j] > 1):
                    count += 1
        return count
