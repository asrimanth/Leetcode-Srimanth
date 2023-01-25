class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # https://leetcode.com/problems/sqrtx/discuss/2635982/Python-(Faster-than-97)-or-Binary-search
        
        low = 0
        high = x
        
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            if square == x or square < x < (mid + 1) * (mid + 1):
                return mid
            elif square > x:
                high = mid - 1
            else:
                low = mid + 1
        return