# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def clearDigits(self, s: str) -> str:
        # Stack approach
        stack = []
        i, n = 0, len(s)
        for char in s:
            if char.isdigit() and len(stack):
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
