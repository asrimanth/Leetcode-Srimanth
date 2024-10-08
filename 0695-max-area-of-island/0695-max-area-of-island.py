class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
            return 0
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    curr_area = dfs(i, j)
                    max_area = max(curr_area, max_area)
        return max_area
