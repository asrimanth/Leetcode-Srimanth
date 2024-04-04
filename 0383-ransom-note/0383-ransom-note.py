# Comparing 2 hashmaps using the collection lib
# Normally, create dicts and the compare elementwise
# Time Complexity: O(m + n)
# Space Complexity: O(m + n)
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_1, map_2 = Counter(ransomNote), Counter(magazine)
        return map_1 <= map_2
