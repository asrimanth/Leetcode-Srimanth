class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Fibonacci Logic
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a+b
        return b
