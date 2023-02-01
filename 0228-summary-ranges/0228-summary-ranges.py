class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        i = 0
        while i<len(nums):
            start = end = i
            while end + 1 < len(nums) and nums[end] + 1 == nums[end+1]:
                end += 1
            if end == start:
                result.append("{}".format(nums[start]))
            else:
                result.append("{}->{}".format(nums[start], nums[end]))
            i = end + 1
        return result