# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        for i, char in enumerate(s):
            if hashmap[char] == 1:
                return i
        return -1
