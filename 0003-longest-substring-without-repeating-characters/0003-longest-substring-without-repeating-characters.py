class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        return self.set_approach(s)

    def set_approach(self, s: str) -> int:
        # Time Complexity: O(n):
        # Space Complexity: O(n)
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] not in char_set:
                max_len = max(max_len, right - left + 1)
                char_set.add(s[right])
            else:
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1
                char_set.add(s[right])
        return max_len
