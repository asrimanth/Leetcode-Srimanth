
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = abs(self.kadane_algo(nums, max))
        min_sum = abs(self.kadane_algo(nums, min))

        return max_sum if max_sum > min_sum else min_sum

    def kadane_algo(self, nums: List[int], criterion) -> int:
        result_sum = nums[0]
        curr_sum = 0

        for num in nums:
            curr_sum = criterion(curr_sum, 0)
            curr_sum += num
            result_sum = criterion(result_sum, curr_sum)
        return result_sum
