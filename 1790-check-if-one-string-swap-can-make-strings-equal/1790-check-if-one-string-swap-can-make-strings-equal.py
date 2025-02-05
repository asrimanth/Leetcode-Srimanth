
from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return self.optimized_approach(s1, s2)
    
    def optimized_approach(self, s1: str, s2: str) -> bool:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        ptr_1, ptr_2 = -1, -1
        n = len(s1)
        diff_count = 0

        for i in range(n):
            # Check diff
            if s1[i] != s2[i]:
                diff_count += 1
                if ptr_1 == -1: ptr_1 = i
                elif ptr_2 == -1: ptr_2 = i
        if diff_count == 0: # No modification
            return True
        elif diff_count == 2 and s1[ptr_2] == s2[ptr_1] and s1[ptr_1] == s2[ptr_2]:
            return True
        return False
    
    def simple_approach(self, s1: str, s2: str) -> bool:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
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
