from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Count sort
        s_count = dict(Counter(s))
        t_count = dict(Counter(t))
        return s_count == t_count