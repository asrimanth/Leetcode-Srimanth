class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Bit manipulation: https://leetcode.com/problems/power-of-two/discuss/948641/Python-O(1)-Solution
        return n>0 and (n & n-1 == 0)