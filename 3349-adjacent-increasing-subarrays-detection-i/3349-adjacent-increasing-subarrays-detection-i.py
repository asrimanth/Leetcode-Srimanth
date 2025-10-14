# Explanation here: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/solutions/7273333/simple-solution-o-n-time-o-1-space-beats-100-solutions-detailed-explanation

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev, curr = 0, 1
        n = len(nums)
        k2 = 2 * k
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                curr += 1
            else:
                prev, curr = curr, 1
            if (prev >= k and curr >= k) or curr >= k2:
                return True
        return False
