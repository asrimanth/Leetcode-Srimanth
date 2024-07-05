# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Approach:
        # Reverse: [[1,2,3],[4,5,6],[7,8,9]] -> [[7,8,9],[4,5,6],[1,2,3]]
        # Transpose: [[7,8,9],[4,5,6],[1,2,3]] -> [[7,4,1],[8,5,2],[9,6,3]]
        # matrix = list(reversed(matrix))
        size = len(matrix)
        # Reverse a matrix: O(n)
        for i in range(size//2):
            matrix[i], matrix[size-i-1] = matrix[size-i-1], matrix[i]
        # Transpose a matrix: O(n^2)
        for i in range(size):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
