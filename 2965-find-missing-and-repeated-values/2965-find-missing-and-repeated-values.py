# Time Complexity: O(N*N) + O(N*log(N))
# Space Complexity: O(N*N)
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        data = {i: 0 for i in range(1, (n*n)+1)}
        for i in range(n):
            for j in range(n):
                idx = grid[i][j]
                data[idx] += 1

        data = sorted(data.items(), key=lambda item: item[1])
        return data[-1][0], data[0][0]
