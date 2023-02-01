from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Count sort
        s_count = Counter(s)
        t_count = Counter(t)
        return s_count == t_count