class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_gain = 0
        curr_gain = 0
        for val in gain:
            curr_gain += val
            max_gain = max(max_gain, curr_gain)
        return max_gain