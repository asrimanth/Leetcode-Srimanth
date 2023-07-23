class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i, char in enumerate(s):
            if char != "*":
                result += char
            else:
                result = result[:len(result)-1]
        return result