class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        m, n = len(word1), len(word2)
        result = ""
        while i < m or j < n:
            char1 = word1[i] if i<m else ""
            char2 = word2[i] if j<n else ""
            result += char1 + char2
            i += 1
            j += 1
        return result
