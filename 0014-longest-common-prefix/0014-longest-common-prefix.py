# Time complexity: O(nlogn)
# Space complexity: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        result = ""
        length = min(len(first), len(last))
        for i in range(length):
            if first[i] == last[i]:
                result += first[i]
            else:
                break
        return result