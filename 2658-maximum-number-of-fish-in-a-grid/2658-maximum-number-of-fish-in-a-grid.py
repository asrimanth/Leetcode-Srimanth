from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        return self.my_solution(grid)
    
    def my_solution(self, grid: List[List[int]]) -> int:
        """
        Approach: Use DFS for every non-zero cell.
        Time Complexity: O(M*N)
        Space Complexity: O(M*N)
        """
        rows, cols = len(grid), len(grid[0])
        visited = set()  # visited set outside

        def dfs(r, c):
            fringe = deque([(r, c)])
            total = 0
            while fringe:
                x, y = fringe.popleft()  # Use popleft() for BFS behavior
                if (x, y) in visited:  # Skip if already visited
                    continue
                visited.add((x, y))
                total += grid[x][y]  # Accumulate fish count

                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    a, b = x + di, y + dj
                    if (0 <= a < rows and 0 <= b < cols and grid[a][b] and (a, b) not in visited):
                        fringe.append((a, b))
            return total

        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    result = max(result, dfs(r, c))
        return result


