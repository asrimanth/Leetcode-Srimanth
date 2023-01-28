class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Previous solution
        triangle = [[1]]
        for i in range(1, rowIndex+1):
            binomial_row = [triangle[i-1][0]]
            for j in range(i-1):
                binomial_row.append(triangle[i-1][j] + triangle[i-1][j+1])
            binomial_row.append(1)
            triangle.append(binomial_row)
        return triangle[-1]