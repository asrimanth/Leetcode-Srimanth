# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        N = len(nums)
        curr_sum = nums[0]
        max_sum = curr_sum
        for i in range(1, N):
            curr_sum = curr_sum + nums[i] if nums[i] > nums[i-1] else nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum
