# Time Complexity: O(len(t))
# Space Complexity: O(len(t))
# Since 1 <= s.length, t.length <= 5 * 10^4 is a given constraint
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Count sort
        return Counter(s) == Counter(t)
