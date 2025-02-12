# Time Complexity: O(N*M) + O(N*K*log(K))
# M = Number of digits, K = Number of digits which have the same sum
# Worst case could be if all digits sum up to the same number
# In which case, time complexity is O(N*log(N))
# Space Complexity: O(N) for dict.

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # First we store the digit sums in a dict with indices
        digit_sums = defaultdict(list)
        for idx, num in enumerate(nums):
            res = 0
            temp = num
            while temp:
                res += temp % 10
                temp //= 10
            digit_sums[res].append(num)

        # Loop through digit_sums dict to find the pairs
        max_val = -1
        for dgs, item in digit_sums.items():
            if len(item) > 1:
                temp = sorted(item)[::-1]
                num1, num2 = temp[0], temp[1]
                res = num1 + num2
                max_val = max(max_val, res)

        return max_val
