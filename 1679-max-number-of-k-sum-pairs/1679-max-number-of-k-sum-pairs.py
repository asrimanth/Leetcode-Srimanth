class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = sorted(nums)
        i, j = 0, len(nums)-1

        count = 0
        while i < j:
            if arr[i] + arr[j] == k:
                i += 1
                j -= 1
                count += 1
            elif arr[i] + arr[j] > k:
                j -= 1
            elif arr[i] + arr[j] < k:
                i += 1

        return count
        