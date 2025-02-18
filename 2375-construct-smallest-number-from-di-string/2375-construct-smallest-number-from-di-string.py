# Neetcode solution: https://www.youtube.com/watch?v=GgN8d22BEf0
# Greedy + stack
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res, stack = [], []
        n = len(pattern)

        for i in range(n+1):
            stack.append(i+1)

            while stack and (i == n or pattern[i] == "I"):
                res.append(str(stack.pop()))

        return "".join(res)
