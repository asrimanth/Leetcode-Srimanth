class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # digits = [int(digit) for digit in str(num)]
        # count = 0
        # for digit in digits:
        #     if num % digit == 0:
        #         count += 1
        # return count
        return sum(1 if num % int(d) == 0 else 0 for d in str(num))
        