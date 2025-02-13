# Time Complexity: O(N*log(N))
# Space Complexity: O(N)

import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        count = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            result = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, result)
            count += 1

        return count
