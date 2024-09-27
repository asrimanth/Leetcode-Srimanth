class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.solution(m, n)
    
    def solution(self, m: int, n: int) -> int:
        # Time Complexity: O(M*N)
        # Space Complexity: O(N)
        # https://www.youtube.com/watch?v=IlEsdxuD4lY

        current_row = [1] * n
        for _ in range(m-2, -1, -1): # All rows except the last row
            new_row = [1] * n
            for j in range(n-2, -1, -1): # All cols except the last col
                new_row[j] = new_row[j+1] + current_row[j]
            current_row = new_row
        return current_row[0]
