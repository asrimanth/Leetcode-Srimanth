class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # Two pointer approach
        point1 = 0
        point2 = 0
        result = ""
        while point1 < len(word1) or point2 < len(word2):
            if point1 < len(word1):
                result += word1[point1]
                point1 += 1
            if point2 < len(word2):
                result += word2[point2]
                point2 += 1
        return result
        