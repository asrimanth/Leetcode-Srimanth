from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        data = list(Counter(arr).values())
        return len(data) == len(set(data))