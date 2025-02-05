class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window approach
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            max_len = max(max_len, right - left + 1)
            char_set.add(s[right])
        return max_len
