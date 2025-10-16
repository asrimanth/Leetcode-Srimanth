class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        n = len(nums)
        prev, curr, result = 0, 1, 0
        for i in range(1, n):
            print(prev, curr, result)
            if nums[i] > nums[i-1]:
                curr += 1
            else:
                prev = curr
                curr = 1
            possibility_one = min(prev, curr) # Minimum of 2 subsequences
            possibility_two = curr // 2 # Current sequence can be treated as 2 subsequences
            result = max(result, max(possibility_one, possibility_two))
        return result
