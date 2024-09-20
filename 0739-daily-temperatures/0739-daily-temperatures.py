# Use monotonically increasing stack
# Time Complexity: O(N)
# Space Complexity: O(N)
# https://www.youtube.com/watch?v=cTBiBSnjO3c
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while len(stack) and temp > stack[-1][0]:
                _, top_idx = stack.pop()
                result[top_idx] = idx - top_idx
            stack.append((temp, idx))
        return result
