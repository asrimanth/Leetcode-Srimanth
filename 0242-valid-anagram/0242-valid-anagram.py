from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(sorted(s))
        t_count = Counter(sorted(t))

        return s_count == t_count
