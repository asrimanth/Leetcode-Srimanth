# Time Complexity: O(max(n, k))
# Space Complexity: O(1)

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        n = len(s)
        idx = 0
        while idx < n:
            result.append(s[idx: idx + k])
            idx += k
        # Fill the last in the group
        last_substr = fill * (k-len(result[-1]))
        result[-1] += last_substr
        return result
