class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        result = ""
        for i in range(min(m, n)):
            result += word1[i]
            result += word2[i]

        for j in range(i+1, m):
            result += word1[j]

        for j in range(i+1, n):
            result += word2[j]
        return result
