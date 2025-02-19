# Backtracking approach
# Time Complexity: O(N*(2^N))
# Space Complexity: O(2^N) for recursion.

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ("a", "b", "c")
        result = []

        def backtrack(temp):
            # Base case:
            if len(temp) == n:
                result.append(temp)
                return

            for char in letters:
                if len(temp) > 0 and temp[-1] != char:
                    temp += char
                    backtrack(temp)
                    temp = temp[:-1]
                elif len(temp) == 0:
                    temp += char
                    backtrack(temp)
                    temp = temp[:-1]
            return
        backtrack("")
        if len(result) > k-1:
            return result[k-1]
        return ""
