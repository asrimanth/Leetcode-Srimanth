class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            # Obstacle at start or goal
            return 0
        return self.one_dim_dp(obstacleGrid)
    
    def one_dim_dp(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # Fill the last row first
        dp = [0] * n
        dp[n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j + 1 < n:
                    dp[j] = dp[j] + dp[j+1]

        return dp[0]
    
    def two_dim_dp(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp_table = [[0] * m for _ in range(n)]

        # Fill the last row and col with 1
        for j in range(n):
            dp_table[m-1][j] = 1 if not obstacleGrid[m-1][j] else 0

        for i in range(m):
            dp_table[i][n-1] = 1 if not obstacleGrid[i][n-1] else 0

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j]:
                    dp_table[i][j] = 0
                else:
                    dp_table[i][j] = dp_table[i][j-1] + dp_table[i-1][j]

        return dp_table[0][0]
