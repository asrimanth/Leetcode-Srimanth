class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Use XOR
        # Explanation: https://leetcode.com/problems/single-number/discuss/2778969/Python-XOR-Solution-Fully-Explained-(O(n)-time-O(1)-space)
        result = 0
        for num in nums:
            result ^= num
        return result