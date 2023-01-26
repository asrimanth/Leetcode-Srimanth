import math
class Solution(object):
    
    def combination(self, n, r):
        if r > n:
            return 0
        if r == 0 or r == n:
            return 1
        return self.combination(n-1, r-1) + self.combination(n-1, r)
    
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]
        # Brute Force
        # for n in range(1, numRows):
        #     binomial_exp=[]
        #     for r in range(n+1):
        #         binomial_exp.append(self.combination(n, r))
        #     result.append(binomial_exp)
        # return result
        
        # DP
        for n in range(1, numRows):
            binomial_exp = [result[n-1][0]]
            for r in range(n-1):
                new_element = result[n-1][r] + result[n-1][r+1]
                binomial_exp.append(new_element)
            binomial_exp.append(result[n-1][-1])
            result.append(binomial_exp)
        return result
            