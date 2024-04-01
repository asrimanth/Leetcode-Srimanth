# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len, h_len = len(needle), len(haystack)
        for i in range(h_len-n_len+1):
            if haystack[i:i+n_len] == needle:
                return i
        return -1