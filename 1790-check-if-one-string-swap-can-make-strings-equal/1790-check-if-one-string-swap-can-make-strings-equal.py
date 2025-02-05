# Time Complexity: O(N)
# Space Complexity: O(N)
from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        n = len(s1)
        diff_count = 0
        if Counter(s1) != Counter(s2):
            return False
        for i in range(n):
            # Check diff
            if s1[i] != s2[i]:
                diff_count += 1
        return diff_count == 2
