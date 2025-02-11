class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_list = list(part)
        k = len(part_list)
        for char in s:
            stack.append(char)
            if len(stack) >= k and stack[-k:] == part_list:
                for _ in range(k):
                    stack.pop()

        return "".join(stack)
