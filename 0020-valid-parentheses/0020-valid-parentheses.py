class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(" : ")", "[" : "]", "{" : "}"}
        for char in s:
            if char in pairs.keys():
                stack.append(char)
            if char in pairs.values():
                if len(stack) == 0:
                    return False
                latest = stack.pop()
                if char != pairs[latest]:
                    return False
        
        return True if len(stack) == 0 else False