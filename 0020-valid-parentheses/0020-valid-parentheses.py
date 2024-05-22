# Time complexity: O(n)
# Space complexity: O(n)
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
        
        return True if len(stack)==0 else False
