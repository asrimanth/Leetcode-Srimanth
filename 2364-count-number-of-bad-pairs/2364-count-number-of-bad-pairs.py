class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Approach: store the good pairs first
        # j - i = nums[j] - nums[i] => nums[i] - i = nums[j] - j
        # Hence store nums[i] - i in a dict
        good_pairs_count = dict()
        bad_pairs = 0
        for i, num in enumerate(nums):
            key = num - i
            curr_count = good_pairs_count.get(key, 0)
            bad_pairs += i - curr_count
            good_pairs_count[key] = curr_count + 1
        return bad_pairs
