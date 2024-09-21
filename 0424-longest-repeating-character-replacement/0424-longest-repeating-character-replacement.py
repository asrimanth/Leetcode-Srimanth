# Time Complexity: O(26 * N) ~ O(N)
# Space Complexity: O(26) ~ O(1)
# Sliding window + hashmap
# https://www.youtube.com/watch?v=gqXU1UyA8pk
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        counts = dict()
        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)
            while right-left+1 - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            result = max(result, right-left+1)
        return result
