class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Use XOR
        result = 0
        for num in nums:
            result = result ^ num
        return result