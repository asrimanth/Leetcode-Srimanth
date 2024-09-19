# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in mapping.keys():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                latest = stack.pop()
                if char != mapping[latest]:
                    return False

        return len(stack)==0
