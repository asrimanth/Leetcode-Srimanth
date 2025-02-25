# Neetcode Solution: https://www.youtube.com/watch?v=AIlI-24oC6Q
# Uses Prefix sums
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        curr_sum = 0
        odd_count, even_count = 0, 0
        result = 0
        MOD = 10**9 + 7

        for num in arr:
            curr_sum += num

            if curr_sum % 2: # Odd number
                result = (result + 1 + even_count) % MOD
                odd_count += 1
            else: # Even number
                result = (result + odd_count)
                even_count += 1
        return result
