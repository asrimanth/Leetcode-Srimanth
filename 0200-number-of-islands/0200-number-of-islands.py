from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        return self.bfs_sol(grid)

    def dfs_sol(self, grid: List[List[str]]) -> int:
        # Time Complexity: O(M * N)
        # Space Complexity: O(M * N) for DFS Stack
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                # Mark as visited
                grid[i][j] = "#"
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
            return

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
    
    def bfs_sol(self, grid: List[List[str]]) -> int:
        # Time Complexity: O(M*N)
        # Space Complexity: O(M*N)
        m, n = len(grid), len(grid[0])
        count = 0

        def bfs(i, j):
            fringe = deque([(i, j)])
            neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while fringe:
                i, j = fringe.popleft()
                grid[i][j] = "#" # Mark as visited
                for di, dj in neighbors:
                    r, c = i + di, j + dj
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == "1":
                        grid[r][c] = "#"
                        fringe.append((r, c))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)

        return count
