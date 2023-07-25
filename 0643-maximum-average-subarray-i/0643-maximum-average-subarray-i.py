class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(len(nums)-k):
            curr_sum = curr_sum - nums[i] + nums[i+k]
            max_sum = max(curr_sum, max_sum)
        return float(max_sum) / k