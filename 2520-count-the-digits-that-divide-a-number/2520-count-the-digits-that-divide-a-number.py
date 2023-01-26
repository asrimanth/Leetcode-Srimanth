class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = [int(digit) for digit in str(num)]
        count = 0
        for digit in digits:
            if num % digit == 0:
                count += 1
        return count
        