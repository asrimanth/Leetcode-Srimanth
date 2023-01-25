class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Binary search
        low = 0
        high = num
        
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                high = mid - 1
            else:
                low = mid + 1