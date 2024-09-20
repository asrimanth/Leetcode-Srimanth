# Approach: Maintain the (value, current_min) as a tuple in the stack.
# Time Complexity: O(1)
# Space Complexity: O(N)
from math import inf
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float(inf)

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        self.stack.append((val, self.min))
        return None

    def pop(self) -> None:
        self.stack.pop()
        self.min = self.stack[-1][1] if len(self.stack) else float(inf)

    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()