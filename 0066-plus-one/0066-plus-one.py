class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        digits[-1] += 1
        carry = 0
        for i in range(n-1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
        if carry > 0:
            digits.insert(0, carry)
        return digits