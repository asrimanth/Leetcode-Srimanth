# Time Complexity: O(N*log(N))
# Space Complexity: O(N)

import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        num_sum = sum(nums)
        nums = sorted([-1*num for num in nums])
        expected_sum = num_sum / 2
        count = 0

        while num_sum > expected_sum:
            max_num = -1 * heapq.heappop(nums)
            max_num /= 2
            num_sum -= max_num
            heapq.heappush(nums, -1 * max_num)
            count += 1
        return count
