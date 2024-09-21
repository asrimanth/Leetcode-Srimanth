# Time Complexity: O(N)
# Space Complexity: O(1)
# Two pointer approach
# https://www.youtube.com/watch?v=1pkOgXD63yU
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                # We are buying low and selling high
                curr_profit = prices[right] - prices[left]
                max_profit = max(max_profit, curr_profit)
            else:
                left = right
            right += 1
        return max_profit
