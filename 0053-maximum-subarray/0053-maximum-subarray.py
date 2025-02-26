# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.kadane_algo(nums)

    def kadane_algo(self,  nums: List[int]) -> int:
        max_sum = float("-inf")
        curr_sum = 0

        for num in nums:
            curr_sum = max(curr_sum, 0) # Resets to zero if curr_sum was ever negative
            curr_sum += num # Starts adding from current position
            max_sum = max(max_sum, curr_sum)
        return max_sum
